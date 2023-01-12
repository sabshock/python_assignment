import urllib.request
import re
def get_url(url):
    url = url
    response = urllib.request.urlopen(url)
    webcontent = response.read().decode("UTF-8")
    pattern = re.compile('<.*?>')
    html_strip = re.sub(pattern,"",webcontent)
    print(html_strip)