#!/usr/bin/env python
# coding: utf-8

# #1 html   
# 영화 순위 랭킹 5위까지   
# 랭킹, 제목, 관객수

# In[35]:


import requests
from bs4 import BeautifulSoup
html = requests.get('https://movie.daum.net/ranking/boxoffice/weekly').text
root = BeautifulSoup(html, 'html.parser')

divs = root.select('div.item_poster')

print('박스오피스 순위')
for i in divs:
    rank = i.select('span.rank_num')[0].text
    title = i.select('a.link_txt')[0].text
    screen_out = i.select('span.info_txt')[1].text
    
    print('순위 :', rank, '/','제목:', title, '/', '관객수 :', screen_out[5:])
    if rank == '5':
        break


# #2 json  
# 날씨 rss 찾아서 지역별 구름양, 온도/습도
# 

# In[187]:


import json
f = open('weather_json.json', 'r', encoding='utf-8')
data = f.read()
items = json.loads(data)
f.close()

for item in items:
    for i in range(0, 11):
        city = item['rss']['channel']['item']['description']['body']['location'][i]['city']
        print()
        print(city, '지역')
        for j in range(0, 13):
            time = item['rss']['channel']['item']['description']['body']['location'][i]['data'][j]['tmEf']
            cloud = item['rss']['channel']['item']['description']['body']['location'][i]['data'][j]['wf']
            min_t = item['rss']['channel']['item']['description']['body']['location'][i]['data'][j]['tmn']
            max_t = item['rss']['channel']['item']['description']['body']['location'][i]['data'][j]['tmx']
            mois  = item['rss']['channel']['item']['description']['body']['location'][i]['data'][j]['rnSt']
            print(time, '--', '구름양 :', cloud, '최저온도 :', min_t, '최고온도: ', max_t, '습도: ', mois)
            
    


# #3 xml  
# 날씨 rss 찾아서 지역별 구름양, 온도/습도
# 

# In[74]:


xml = requests.get('https://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108').text
root = BeautifulSoup(xml, 'html.parser')
loc = root.find_all('location')
for i in loc:
    print(i.city.get_text(), '지역 날씨')
    d = i.find_all('data')
    # tmef, rnst 원본에는 tmEf, rnSt 이나 대문자로 하면 오류 
    for j in d:
        print(j.tmef.string, '-', '구름양 :', j.wf.string, '/', '최저온도',j.tmn.string, '/', '최고 온도 :', j.tmx.string,  '/', '습도 :', j.rnst.string, '%')
        


# #4 테이블  
# 네이버 주식 시황 종목 코드 파라메터로 받아서 그 종목의 시황 정보 출력 함수

# In[76]:


import requests
import pandas as pd

def getByCode(code):
    url='https://finance.naver.com/item/sise_day.nhn?code='+code
    html = requests.get(url, headers={'User-agent': 'Mozilla/5.0'}).text
    a = pd.read_html(html)[0]
    a = a.dropna()
    return a

getByCode('004800')


# #5 csv  
# 강릉시 버스 정보  
# 버스 번호 입력시 버스의 기점과 종점을 출력해주는 함수

# In[141]:


import pandas as pd

def bus(number):
    data = pd.read_csv('버스노선정보.csv', encoding='cp949')
    isTrue = data['노선명'] == number
    
    d1 = data[isTrue]
    d2 = d1['기점정류장']
    d3 = d1['종점정류장']
    
    s = []
    e = []
    for i in d2:
        s.append(i)
        
    for j in d3:
        e.append(j)
    
    for i in range(len(s)):
        print(number, '번 버스 노선의 기점과 종점은', s[i], '/', e[i])
    
    
bus('207')

