#!python
from BeautifulSoup import BeautifulSoup
import requests
import urlparse



def requesturi(url):
    try:
        return requests.get(url, timeout=2)
    except requests.exceptions.ConnectionError:
        pass

target_url = "http://10.0.2.8/mutillidae/index.php?page=dns-lookup.php"
response = requesturi(target_url)

#Extract all forms
parsed_html = BeautifulSoup(response.content)
forms_list = parsed_html.findAll("form")
#print(len(forms_list))

#Extract all inputs and attributes from forms_list.
for form in forms_list:
    action = form.get("action")
    post_url = urlparse.urljoin(target_url,action) #Buildin from relative url to full url
    method = form.get("method")
    input_list = form.findAll("input")
    post_data = {}
    for input in input_list:
        input_name = input.get("name")
        input_type = input.get("type")
        input_value = input.get("value")
        if input_type == "text":
            input_value = "test"
        post_data[input_name] = input_value
    result = requests.post(post_url, data = post_data)
    #print(result.content)
    #print(post_data)