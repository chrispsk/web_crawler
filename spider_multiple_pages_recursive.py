import requests
import re
import urlparse

target_url = "http://10.0.2.8/mutillidae/"
target_links = []

def extract_links_from(url):
    response = requests.get(url)
    html = response.content
    return re.findall('(?:href=")(.*?)"', html) #non-greedy (.*?)

def crawl(url):
    links = extract_links_from(url)
    for link in links:
        link = urlparse.urljoin(url, link) #fix relative links. Automatically keep the good ones.
        #for links like: http://10.0.2.8/mutillidae/prod/#tab1 | http://10.0.2.8/mutillidae/prod/#tab2
        if "#" in link:
            link = link.split("#")[0] #store only first part
        #Keep only the url for this sites + uniques
        if target_url in link and link not in target_links:
            target_links.append(link) #At this moment we know this link is unique
            print(link)
            crawl(link) #CALL HIMSELF

crawl(target_url)