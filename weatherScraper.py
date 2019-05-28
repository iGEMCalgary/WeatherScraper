import requests
import csv
#Scrapes weather information from website
#Creates a CSV file with data
from bs4 import BeautifulSoup

#page = requests.get ("https://weather.com/en-CA/weather/hourbyhour/l/652a7263c23cc4e132305f4820560f34e9c904523b469ccb5be3d1381ee08c28")
page=requests.get("https://weather.com/en-CA/weather/tenday/l/652a7263c23cc4e132305f4820560f34e9c904523b469ccb5be3d1381ee08c28")
soup = BeautifulSoup (page.content, "html.parser")

all = soup.find("div",{"class":"locations-title ten-day-page-title"}).find("h1").text

table = soup.find_all("table",{"class":"twc-table"})
listOfWeatherByDay=[]

#get all info from the webpage using the html DOM
csv_columns = ['Day','Description','High(°C)','Low(°C)','Precipitation(%)','Wind(km/h)','Direction','Humidity(%)']
for items in table:
    for i in range (len(items.find_all("tr"))-1):
                    d = {}
                    d["Day"]=items.find_all("span",{"class":"day-detail clearfix"})[i].text

                    d["Description"] = items.find_all("td",{"class":"description"})[i].text

                    d["High(°C)"],d["Low(°C)"],empty = items.find_all("td",{"class":"temp"})[i].text.split('°')

                    d["Precipitation(%)"] = items.find_all("td",{"class":"precip"})[i].text.split('%')[0]

                    d["Direction"],d["Wind(km/h)"],empty = items.find_all("td",{"class":"wind"})[i].text.split()

                    d["Humidity(%)"] = items.find_all("td",{"class":"humidity"})[i].text.split('%')[0]
#                    if(temp.find("snow") >= 0 or temp.find("Snow")>=0):
#                        d["Snow?"]=True
#                    else:
#                        d["Snow?"]=False


                    listOfWeatherByDay.append(d)
#debug
print (listOfWeatherByDay[0])

#Create SCV file
csv_file = "output.csv"
try:
    with open(csv_file, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        for data in listOfWeatherByDay:
            writer.writerow(data)
except IOError:
    print("I/O error")
#        day = str(item)[10:15]
#        description = str(item)[27:-1]
#        f.write("%s,%s\n" %(day,description))