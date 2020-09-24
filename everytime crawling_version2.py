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
import pandas as pd
# 라이브러리 불러오기

kma = Kkma()

chromedriver = 'C:\dataset\chromedriver.exe'
driver = webdriver.Chrome(chromedriver)
# selenium 라이브러리 기본 작업

driver.get('https://chungbuk.everytime.kr//login')
# 크롤링 할 홈페이지 가져오기
driver.find_element_by_name("userid").send_keys("~~")
# 태그의 네임이 userid 인 element 가져오고 "내 아이디" 입력
driver.find_element_by_name("password").send_keys("")
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

req = driver.page_source
html = BeautifulSoup(req, 'html.parser')
infos = html.select('div.articles')

# 엑셀파일 열기
data = pd.read_csv("Lecture_list(2020).csv")
# 엑셀파일 열기
lecture = data['과목명']
teacher = data['담당교수']

#검색 함수
def search():
#lecture 를 keyword에 입력
#과목하나랑 매칭되는 과목을 검색
    for i in range(len(lecture)):
        keword = lecture[i]
        req1 = driver.page_source
        html1 = BeautifulSoup(req1, 'html.parser')
        #infos1 = html1.select('div.articles')
        driver.find_element_by_name('keyword').send_keys('')
        clip1_pro = html1.select(' a.lecture > h3 > p.professor ')
        for pro in range(len(clip1_pro)):
            #교수랑 매칭되는 부분 select 한다
            for i in range(len(teacher)):
                if clip1_pro[pro] == teacher[i]:
                    # div>a[pro]
                    # pro부분을 select하고 그 홈페이지로 들어간다
                    # 검색 키워드 입력, 실행
                    """
                    route = "div.lectures > a[]"
                    new_route = route[:18] + pro + route[18:]
                    clip1_list = html1.select('div.rating > div.details > p')
                    """
                    driver.find_element('div.lecture')[pro].click()




"""
#별점 따오는 함수

ratings_list = []

def crawling():
    clip1_list = html.select('div.rating > div.details > p')
    for i in range(4):
        ratings_list = clip1_list[i].find('span')
    clip1_text = html.select(' div.r')
    clip1_date = html.select('a > p.info > span')
    clip1_text = html.select('a > p.text')
    for item in zip(clip1_head, clip1_date, clip1_text):

        info_list.append({
            'head': item[0].text,
            'data': item[1].text,
            'text': item[2].text,
        })


data = pd.DataFrame(info_list)
print(data)
data.to_csv('everytime1.csv')
"""
driver_quit = driver.quit()
