import time
import bs4
import urllib.request
import ssl
import pymysql
import re
from tkinter import *

ssl_context = ssl.SSLContext()
ssl_context.verify_mode = ssl.CERT_NONE
area,temp,sky= "","",""
null = None
## 함수 선언 부분
def insertData(area,temp,sky) :
    con, cur = None, None
    data1, data2, data3 = "", "", ""
    sql=""

    con = pymysql.connect(host='127.0.0.1', user='root', password='mysql', database='nateNewsLive', charset='utf8')
    cur = con.cursor()

    data1 = area; 
    data2 = sky; 
    data3 = temp; 
    try :
        
        print(null)
        print(data1)
        print(data2)
        print(data3)
        sql = "INSERT INTO naverWeather (area,temp,sky)  VALUES('"+ data1 + "','" + data3 + "','" + data2 +"')"
        cur.execute(sql)
        
    except :
        print("예외 발생")
        # messagebox.showerror('오류', '데이터 입력 오류가 발생함')
    else :
        print("성공")
        # messagebox.showinfo('성공', '데이터 입력 성공')
    con.commit()
    con.close()
##

naverWeatherUrl = "https://weather.naver.com/today/08110580"
while True :
    htmlObject = urllib.request.urlopen(naverWeatherUrl,context=ssl_context)
    webPage = htmlObject.read()
    bsObject = bs4.BeautifulSoup(webPage, 'html.parser')
    tag_list = bsObject.findAll('div', {'class': 'card card card_today_weather'})

    print('###### 실시간 뉴스 속보 #######')
    print(tag_list)
    num = 1
    for tag in tag_list :

        area = tag.find('strong', {'class': 'location_name'}).text
        
        temp = "현재 온도 " + tag.find('span',{'class':'blind'}).text.strip()

        sky = tag.find('span', {'class': 'weather'}).text
        insertData(area, temp, sky)

    time.sleep(3)