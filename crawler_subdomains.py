import requests

#Communicate with websites
url = "mail.google.com"
# try:
#     get_response = requests.get("http://"+url)
#     print(get_response)
# except requests.exceptions.ConnectionError:
#     pass

def requesturi(url):
    try:
        return requests.get("http://" + url + "." + "google.com", timeout=2)
    except requests.exceptions.ConnectionError:
        pass

#print(requesturi(url))
subdomain_ok = []
with open("subdomains-wodlist.txt", "r") as words:
    for word in words:
        new_word = word.strip()
        #test_url = new_word + ".google.com"
        #print("calculating " + new_word)
        response = requesturi(new_word)
        if response:
            print("[+] Subdomain Found at: " + new_word)
