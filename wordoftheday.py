
import sys    #Importing the System Library
from bs4 import BeautifulSoup
import os

#Downloading entire Web Document (Raw Page Content)
def download_page(url):
    version = (3,0)
    cur_version = sys.version_info
    if cur_version >= version:     #If the Current Version of Python is 3.0 or above
        import urllib.request    #urllib library for Extracting web pages
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
            req = urllib.request.Request(url, headers = headers)
            resp = urllib.request.urlopen(req)
            respData = str(resp.read())
            print("success")
            return respData
        except Exception as e:
            print(str(e))
    else:                        #If the Current Version of Python is 2.x
        import urllib2
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
            req = urllib2.Request(url, headers = headers)
            response = urllib2.urlopen(req)
            page = response.read()
            return page
        except:
            return"Page Not found"

perPage =100
page = 1
count = 0
url = 'https://art19.com/shows/merriam-websters-word-of-the-day?page='+page+'&perPage='+perPage#https://art19.com/shows/merriam-websters-word-of-the-day?page=1&perPage=100
print("opening url " + url)
raw_html = (download_page(url))
soup = BeautifulSoup(raw_html,"lxml")
div_content = soup.find("div", {"class": "episode-list"})
ite=[]
for li in div_content.findAll('ember-view'):
    #print(str(li).findAll('title'))
    #ite.append(str  (li.text.encode("utf-8")).split(" ")[0].replace("b'",""))
    print(li.text.encode("utf-8"))

# print(ite)
ul_content=[]

            # print(immg)


print("end")
print("count" +str(count))
# print("------------------------------------------------------------------------------------------------------------------------")
# print(str(div_content))
