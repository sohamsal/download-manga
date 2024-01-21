import manganelo as manganelo
import os
from datetime import datetime, timedelta, date
import requests
from bs4 import BeautifulSoup
import calendar


mangaName = input("What manga do you want to download?\n")
results = manganelo.get_search_results(f"{mangaName}")
print("Loading chapters...")
first = results[0]
mangaURL = first.url
page = requests.get(mangaURL)
chapters = first.chapter_list


soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find("span", {"class": "stre-value"})
temp_holder = results.text


lastUpdateTime = results.text[0:11]
lastUpdate_month = list(calendar.month_abbr).index(lastUpdateTime[0:3]) # month 
lastUpdate_day = lastUpdateTime[4:6] # day
lastUpdate_year = lastUpdateTime[7:11] # year
lastUpdateActualTime = results.text[14:19] # hours and min
lastUpdate_hour = lastUpdateActualTime[0:2] # hours
lastUpdate_minutes = lastUpdateActualTime[3:5] #minutes
lastUpdateDateTimeUseThis = datetime(int(lastUpdate_year), int(lastUpdate_month), int(lastUpdate_day))


currentDateTimeText = datetime.now().strftime('%Y-%m-%d-%H:%M')
current_year = currentDateTimeText[0:4]
current_month = currentDateTimeText[5:7]
current_day = currentDateTimeText[8:10]
current_hour = currentDateTimeText[11:13]
current_minutes = currentDateTimeText[14:16]
curentDateTimeUseThis = datetime(int(current_year), int(current_month), int(current_day))

def numOfDays(date1, date2):
    return (date2-date1).days

print(numOfDays(lastUpdateDateTimeUseThis, curentDateTimeUseThis), "days since the last chapter")
print("There are " + str(len(chapters)) + " chapters to choose from for this manga")


chap_one = chapters[0]

count = 0
for chap in chapters:
    count += 1

last = chapters[count-1]


chapNumber = str(input("What chapter do you want to download? (Provide a number, or say last for the latest chapter)\n"))
if chapNumber == "1":
    print("Downloading chapter...the console will print out successfully downloaded when it finishes")
    download = chap_one.download(path = f"[ADD UR FILE PATH HERE]{mangaName}{chap_one.title}.pdf")
elif chapNumber == "last":
    print("Downloading chapter...the console will print out successfully downloaded when it finishes")
    download = last.download(path = f"[ADD UR FILE PATH HERE]{mangaName}{last.title}.pdf")
else:
    intVersion = int(chapNumber)-1
    print("Downloading chapter...the console will print out successfully downloaded when it finishes")
    download = chapters[intVersion].download(path = f"[ADD UR FILE PATH HERE]{mangaName}{chapters[intVersion].title}.pdf")
    
print("Successfully downloaded!")
os.startfile("[ADD UR FILE PATH HERE]")
