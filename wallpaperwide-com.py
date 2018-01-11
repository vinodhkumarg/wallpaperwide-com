
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

count = 0
url = 'http://wallpaperswide.com'
print("opening url " + url)
raw_html = (download_page(url))
soup = BeautifulSoup(raw_html,"lxml")
div_content = soup.find("div", {"class": "sidebox-body-cnt"})
ite=[]
for li in div_content.findAll('li'):
        #print(str(li).findAll('title'))
        ite.append(str(li.text.encode("utf-8")).split(" ")[0].replace("b'",""))

# print(ite)
ul_content=[]
for it in ite:
    uri=url+"/"+it+"-desktop-wallpapers/page/12";
    print("opening url "+uri)
    page=(download_page(uri))
    soup = BeautifulSoup(page, "lxml")
    images_urls = soup.findAll("img", {"class": "thumb_img"})

    # make a search keyword  directory
    try:
        os.makedirs(it)
    except OSError as e:
        if e.errno != 17:
            raise
            # time.sleep might help here
        pass

    for img in images_urls:
        img_url = img.get('src')
        # This allows you to write all the links into a test file. This text file will be created in the same directory as your code. You can comment out the below 3 lines to stop writing the output to the text file.
        info = open('output1.txt', 'a')  # Open the text file called database.txt
        info.write(img_url)  # Write the title of the page
        img_url = str(img_url).replace("thumbs","download").replace("t1","wallpaper-1366x768")
        info.write(img_url)  # Write the title of the page
        info.close()
        print(img_url)
        try:
            import urllib
            img_name = img_url.replace("http://hd.wallpaperswide.com/download/","")
            img_name = img_name.replace("-1366x768.jpg","")
            req = urllib.request.Request(img_url, headers={
                "User-Agent": "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"})
            response = urllib.request.urlopen(req, None, 15)
            output_file = open(it + "/" + img_name + ".jpg", 'wb')

            data = response.read()
            output_file.write(data)
            response.close();
            count = count+1
            print("completed ====> "+img_name)
        except IOError:  # If there is any IOError
            print("IOError on image " + img_url)
        except urllib.error.HTTPError as e:  # If there is any HTTPError
            print("HTTPError " + img_url)
        except urllib.error.URLError as e:
            print("URLError " + img_url)
    # print(immg)


print("end")
print("count" +str(count))
# print("------------------------------------------------------------------------------------------------------------------------")
# print(str(div_content))