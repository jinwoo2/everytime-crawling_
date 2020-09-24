from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import pandas as pd
import time
from konlpy.tag import Kkma
import openpyxl
from selenium.webdriver.common.keys import Keys
# 라이브러리 불러오기

kma = Kkma()

chromedriver = 'C:\dataset\chromedriver.exe'
driver = webdriver.Chrome(chromedriver)
# selenium 라이브러리 기본 작업

driver.get('https://chungbuk.everytime.kr//login')
# 크롤링 할 홈페이지 가져오기
driver.find_element_by_name("userid").send_keys("~~")
# 태그의 네임이 userid 인 element 가져오고 "내 아이디" 입력
driver.find_element_by_name("password").send_keys("~~~")
# 태그의 네임이 password 인 element 가져오고 "비밀번호" 입력
driver.find_element_by_tag_name("input").send_keys(Keys.RETURN)
# 로그인 버튼 찾고 클릭

time.sleep(2)
# driver.find_element_by_xpath('//*[@id="container"]/div[3]/div[4]/div/h3/a').click()

driver.find_element_by_xpath('//*[@id="container"]/div[3]/div[4]/div/h3/a').click()
time.sleep(5)
# driver.find_element_by_css_selector('#container > div.wrap.articles > div.pagination > a').click()

driver.find_element_by_xpath('//*[@id="sheet"]/ul/li[3]/a').click()  # 광고 닫기 버튼
time.sleep(2)
info_list = []

for i in range(25):
    time.sleep(0.3)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(0.2)


req = driver.page_source
html = BeautifulSoup(req, 'html.parser')
infos = html.select('div.articles')
#수정장소

clip1_head = html.select(' a.article > h3')
clip1_date = html.select('a > p.info > span')
clip1_text = html.select('a > p.text')


def plus_page():
    for item in zip(clip1_head, clip1_date, clip1_text):

        info_list.append({
            'head': item[0].text,
            'data': item[1].text,
            'text': item[2].text,
        })

for i in range(8):
    plus_page()

data = pd.DataFrame(info_list)
print(data)
data.to_csv('everytime11.csv')

driver_quit = driver.quit()
