#from fileinput import filename
#from itertools import count
import urllib.request
#from wsgiref import headers
import pandas as pd

data = pd.read_excel(r'testing_excel.xlsx')
print(data.shape)

urls = data['image']

count = 1

#security check issue fix
opener = urllib.request.URLopener()
opener.addheader('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36')


for url in urls:
    filename, headers = opener.retrieve(url, "./images_AWS/"+str(count)+".jpg")

    count = count+1
    print(url, "Downloaded...")

print("Download finished...")