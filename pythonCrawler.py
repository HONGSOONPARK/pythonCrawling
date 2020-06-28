# -*- coding: utf-8 -*- 

import requests
import time
import pymysql


from bs4 import BeautifulSoup


from urllib.parse import quote_plus    # 한글 텍스트를 퍼센트 인코딩으로 변환

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait   # 해당 태그를 기다림
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException    # 태그가 없는 예외 처리


# source = requests.get("https://www.naver.com").text
# soup = BeautifulSoup(source, "html.parser")
# hotKeys = soup.select("span.ah_k")
# index = 0
# print(soup.html)
# for key in hotKeys:
#     index += 1
#     print(str(index) + ", " + key.text)    
#     if index >= 20:
#         break

options = webdriver.ChromeOptions()
options.add_argument('headless')
# options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")
# 혹은 options.add_argument("--disable-gpu")
options.add_argument('lang=ko_KR')    # 언어 설정

driver = webdriver.Chrome('/home/hs/Python/py/chromedriver', chrome_options=options)
driver.implicitly_wait(3)


 



try:    # 정상 처리

    driver.get('https://google.com')
    # element = WebDriverWait(driver, 3).until(
      #  EC.presence_of_element_located((By.CLASS_NAME, 'list_title'))
    #)    # 해당 태그 존재 여부를 확인하기까지 3초 정지
    
    time.sleep(2) # 웹페이지를 불러오기 위해 2초 정지
    # test_data = driver.find_element_by_class_name('gb_g')

    test_data = driver.find_element_by_xpath('/html/body/div/div[1]/div/div/div/div[1]/div[1]/a')

    


    # MySQL Connection 연결
    conn = pymysql.connect(host='localhost', user='testhong', password='1234',
                        db='testhong', charset='utf8')
    
    # Connection 으로부터 Cursor 생성
    curs = conn.cursor()
    
    # SQL문 실행
    sql = "select * from list"
    curs.execute(sql)
    
    # 데이타 Fetch
    rows = curs.fetchall()
    print(rows)     # 전체 rows
    # print(rows[0])  # 첫번째 row: (1, '김정수', 1, '서울')
    
    
    # Connection 닫기

    print(test_data.text)

except TimeoutException:    # 예외 처리
    print('타임아웃 발생')

finally:    # 정상, 예외 둘 중 하나여도 반드시 실행
    driver.quit()
    conn.close()



print('크롤링 끝')

