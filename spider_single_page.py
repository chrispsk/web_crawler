import requests
import re
import urlparse

#REPLACE RELATIVE LINKS WITH LINKS
#IGNORE LINKS THAT ARE NOT PART OF THE WEBSITE TARGETED
#Unique Links
def return_links(url):
    response = requests.get(url)
    html = response.content
    return re.findall('(?:href=")(.*?)"', html) #non-greedy (.*?)
target_links = []
links = return_links("http://10.0.2.8/mutillidae/")
for link in links:
    link = urlparse.urljoin("http://10.0.2.8/mutillidae", link) #fix relative links. Automatically keep the good ones.
    #for links like: http://10.0.2.8/mutillidae/prod/#tab1 | http://10.0.2.8/mutillidae/prod/#tab2
    if "#" in link:
        link = link.split("#")[0] #store only first part
    #Keep only the url for this sites + uniques
    if "http://10.0.2.8/mutillidae" in link and link not in target_links:
        target_links.append(link)
        print(link)