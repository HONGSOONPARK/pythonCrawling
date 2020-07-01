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
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_argument('headless')
# options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu") # 혹은 options.add_argument("--disable-gpu")

options.add_argument('lang=ko_KR')    # 언어 설정
driver = webdriver.Chrome('/home/hs/Python/py/chromedriver', chrome_options=options)
driver.implicitly_wait(3)

wait = WebDriverWait(driver, 10)

# MySQL Connection 연결
conn = pymysql.connect(host='localhost', user='testhong', password='1234', db='testhong', charset='utf8') 

try:    # 정상 처리

    driver.get('https://google.com')

    time.sleep(2) # 웹페이지를 불러오기 위해 2초 정지

    # 검색창 # 해당 태그 존재 여부를 확인하기까지 3초 정지
    element = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[2]/form/div[2]/div[1]/div[1]/div/div[2]/input')))
  
    # 검색창에 키워드 입력
    keyword = "공덕역 밥집"
    element.send_keys(keyword)

    # 엔터키 입력
    element.send_keys(Keys.ENTER)


    # 검색 버튼
    # element = driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[3]/center/input[1]')
    # element.click();

    time.sleep(1)

    # 장소 더 보기 버튼
    element = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[5]/div[2]/div[9]/div[1]/div[2]/div/div[2]/div[2]/div/div/div[1]/div/div[2]/div/div[4]/div[3]/div/div/a/div/span')))
    element.click()

    time.sleep(5)


    element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="rllhd__fldhc"]/div/div/div/div/div[1]/div/div[1]/div')))
    
    # print('장소리스트 들어옴 : '+ element.text)
    # print('장소리스트 들어옴 : '+ driver.current_url)

    # 장소 리스트
    element = driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[8]/div[1]/div[2]/div/div[2]/div[2]/div/div/div/div/div[2]/div/div/div[1]/div[4]')
    

    #element = driver.find_elements_by_xpath('//*[@id="rl_ist0"]/div[1]/div[4]/div')
    # t1 = driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[8]/div[1]/div[2]/div/div[2]/div[2]/div/div/div/div/div[2]/div/div/div[1]/div[4]/div[5]/div/div[3]/div/a/div/div[2]/div')
    #print(element.text)
    

    # wrap = driver.find_element_by_xpath('//*[@id="rl_ist0"]')
   

    print('============================================')
    page_count = driver.find_elements_by_xpath('//*[@id="rl_ist0"]/div[1]/div[4]/div')

    i = 0

    while i < len(page_count) :
        i += 1
        

        # test = 'div:nth-child(%d) > div > div.uMdZh.rl-qs-crs-t.mnr-c > div > a > div > div.dbg0pd > div' % i

        txt =f'//*[@id="rl_ist0"]/div[1]/div[4]/div[{i}]'
        
        print(str(txt))
        wrap = driver.find_element_by_xpath(txt)
        wait_txt = WebDriverWait(wrap, 1)
        print(wrap.text)

        try:
            tt = wait_txt.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div > div.uMdZh.rl-qs-crs-t.mnr-c > div > a > div > div.dbg0pd > div')))
            print(tt.text)    
        except Exception:
            print('except')
        finally:
            print('============================================')    

        
        # store_div = wrap.find_element_by_css_selector(str(test))

        # store_div = wait.until(EC.element_to_be_clickable((By.XPATH, str(txt))))
        # store_div.click()

        # store_title = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="akp_tsuid30"]/div/div[1]/div/div/div/div[1]/div/div[1]/div/div[1]/div/div[1]/div/div[1]/div/span')))
        
        # store_name = store_div.find_element_by_xpath('//*[@class="dbg0pd"]')
        # if store_title is not None :
        #     print(store_title.text)
            
        #rl_ist0 > div.rl_tile-group > div.rlfl__tls.rl_tls > div:nth-child(1) > div
        # print(store_name.text)

        time.sleep(1)



        # st = wrap.find_element_by_css_selector('div:nth-child(2) > div > div.uMdZh.rl-qs-crs-t.mnr-c > div > a > div > div.dbg0pd > div')
        # print(st.text)
    

    
    
    

    # for buyer in element:
    #     tt = buyer.find_element_by_xpath('//*[@id="rl_ist0"]/div[1]/div[4]/div[5]/div/div[3]/div/a/div/div[2]/div/text()[1]')
    #     # if(tt is not None) :
    #     print(tt.text)

 

    #list = element.find_element_by_xpath('div[1]/div/div[2]/div/a/div') 
    
    # tt = element.find_element_by_css_selector('div:nth-child(1) > div > div.uMdZh.rl-qs-crs-t.mnr-c > div > a > div > div.dbg0pd > div')
                        
                        

    # print(list.text)
    # for item in list :
    #     print(item.text)
    # print(len(list))

    # print(len(element))
    
    index = 0
   
    # for p in body.find_elements_by_tag_name('div'):
    #     print (p.text)


    # while index < len(element) :
    #     index += 1

    #     lists = element[index].find_element_by_xpath('//div/div[2]/div/a/div/div[2]/div')

    #     print (lists.text)
        # for p in lists.find_element_by_xpath('div'):
        #     print (p.text)
        
        #rl_ist0 > div.rl_tile-group > div.rlfl__tls.rl_tls > div:nth-child(1) > div > div.uMdZh.rl-qs-crs-t.mnr-c.rllt__local-item-selected > div > a > div > div.dbg0pd > div
        # //*[@id="rl_ist0"]/div[1]/div[4]/div[1]/div/div[2]/div/a/div/div[2]/div
        # for p in rs.find_element_by_xpath('a'):
        #     print (p.text)
        

           
    # print(len(list))
        
        


        
    # for key in box:
    #     index += 1
    #     box.find_element_by_xpath('//*[@id="rl_ist0"]/div[1]/div['+index+']/div[1]/div/div[2]/div/a/div') 
    #     print(str(index) + ", " + key.text)    
            
        # if index >= search_list.length:
        #     break

    # Connection 으로부터 Cursor 생성
    curs = conn.cursor()
    
    # SQL문 실행

    # INSERT INTO google_list  (name, code1, code2, code3, addr, tel, time, star, del_yn) VALUES  ('test', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
    sql = "select 1 from dual"
    curs.execute(sql)
    
    # 데이타 Fetch
    rows = curs.fetchall()
    print(rows)     # 전체 rows
    # print(rows[0])  # 첫번째 row: (1, '김정수', 1, '서울')
    
    # Connection 닫기
except TimeoutException:    # 예외 처리
    print('타임아웃 발생')

finally:    # 정상, 예외 둘 중 하나여도 반드시 실행
    driver.quit()
    conn.close()




print('크롤링 끝')

