import requests

#Communicate with websites
#url = "mail.google.com"
# try:
#     get_response = requests.get("http://"+url)
#     print(get_response)
# except requests.exceptions.ConnectionError:
#     pass

def requesturi(url):
    try:
        return requests.get("http://" + "10.0.2.8/mutillidae/" + url, timeout=2)
    except requests.exceptions.ConnectionError:
        pass

#print(requesturi(url))
subdomain_ok = []
with open("files-and-dirs-wordlist.txt", "r") as words:
    for word in words:
        new_word = word.strip()
        #test_url = new_word + ".google.com"
        #print("calculating " + new_word)
        response = requesturi(new_word)
        if response:
            print("[+] Dir Found at: " + new_word)
