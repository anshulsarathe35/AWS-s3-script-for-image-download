#from fileinput import filename
#from itertools import count
import urllib.request
#from wsgiref import headers
import pandas as pd

data = pd.read_excel(r'testing_excel.xlsx')  ##your excel sheet containing images
print(data.shape)

urls = data['image']

count = 1

#security check issue fix
opener = urllib.request.URLopener()
opener.addheader('User-Agent', 'your user agent')
#your user agent 


for url in urls:
    filename, headers = opener.retrieve(url, "./images_AWS/"+str(count)+".jpg")
    #./images/ (your image folder where your images are downloaded)

    count = count+1
    print(url, "Downloaded...")

print("Download finished...")
