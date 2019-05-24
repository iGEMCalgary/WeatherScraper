import requests
import csv
#Scrapes weather information from website 
#Creates a CSV file with data
from bs4 import BeautifulSoup

page = requests.get ("https://weather.com/en-CA/weather/hourbyhour/l/652a7263c23cc4e132305f4820560f34e9c904523b469ccb5be3d1381ee08c28")
soup = BeautifulSoup (page.content, "html.parser")

all = soup.find("div",{"class":"locations-title hourly-page-title"}).find("h1").text

table = soup.find_all("table",{"class":"twc-table"})
l=[]

csv_columns = ['Time','Snow']

for items in table:
    for i in range (len(items.find_all("tr"))-1):
                    d = {}
                    d["Time"]=items.find_all("span",{"class":"dsx-date"})[i].text
                    temp = items.find_all("td",{"class":"description"})[i].text
                    if(temp.find("snow") >= 0 or temp.find("Snow")>=0):
                        d["Snow?"]=True
                    else:
                        d["Snow?"]=False
                    
                    
                    l.append(d)
print (l[0])
with open('output.csv','w') as f:
    for item in l:
        
        time = str(item)[10:15]
        snow = str(item)[27:-1]
        f.write("%s,%s\n" %(time,snow))