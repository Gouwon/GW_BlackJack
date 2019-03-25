## 셀레니움으로 접근하여 지원 번호 수집.

def access_court_auction_site(url):
    from selenium import webdriver
    from selenium.webdriver.support.ui import Select
    import os
    import time
    

    if os.name == 'nt':
        driver = webdriver.Chrome('C:\Program Files (x86)\chromedriver_win32/chromedriver.exe')
    elif os.name == 'posix':
        driver = webdriver.Chrome('/Users/mac/workspace/chromedriver')
    else:
        print("Not supported OS")
        exit()

    ## 법원경매 홈페이지 접속
    driver.get(url)
    driver.implicitly_wait(15)

    ## 법원경매 프레임 변경
    main = driver.switch_to.default_content()

    ## 법원경매 팝업창 닫기
    handles = len(driver.window_handles)
    if handles != 1:
        for i in range(1, handles):
            if i == handles:
                continue
            driver.switch_to.window(driver.window_handles[i])
            driver.close()
        driver.switch_to.window(driver.window_handles[0])

    # print("==========",driver.find_elements_by_tag_name("frame"))

    driver.switch_to.frame(driver.find_elements_by_tag_name("frame")[0])

    

    ## 법원경매 매각결과검색 페이지 접속
    driver.execute_script( open('../jquery-3.3.1.js').read() )
    driver.execute_script("$('#menu_s_2_son > div.son_h > ul > li:nth-child(8) > a').click();")
    driver.implicitly_wait(20)

    with open('./results/xx.html', 'w') as file:
        file.write(driver.page_source)

    driver.find_element_by_xpath('//*[@id="idMulStatcd"]/option[2]').click()
    driver.implicitly_wait(3)
    driver.find_element_by_xpath('//*[@id="idLevel1"]').click()
    driver.find_element_by_xpath('//*[@id="idLevel1"]/option[4]').click()
    driver.implicitly_wait(3)
    driver.find_element_by_xpath('//*[@id="idLevel2"]/option[2]').click()
    driver.implicitly_wait(3)
    driver.find_element_by_xpath('//*[@id="idLevel3"]/option[2]').click()    
    driver.implicitly_wait(3)
    driver.find_element_by_xpath('//*[@id="idJiwonNm"]').click()
    driver.implicitly_wait(3)
    driver.find_element_by_xpath('//*[@id="idJiwonNm"]/option[60]').click()
    driver.implicitly_wait(3)
    driver.find_element_by_xpath('//*[@id="contents"]/form/div/a[1]').click()
    driver.implicitly_wait(3)



    ## 법원경매 매각결과목록 페이지 접속

    driver.find_element_by_xpath('//*[@id="contents"]/div[4]/form[1]/table/tbody/tr[1]/td[2]/a').click()

    # p=driver.get_cookies()
    # print(p)
    # print(len(p))

    ## 자바스크립트 실행하여서 쿠키나 헤더를 가지고 와보자... jiwonNm encoded를 최종적으로 가지고 있거나, 상세 페이지로 접근하여야 한다. ==> requests 모듈 사용하려는 전제 하에서...
    time.sleep(5)
    p = driver.execute_script('return document.cookie')
    print(p)

    with open('./results/xx.html', 'w') as file:
        file.write(driver.page_source)

    user_check = input("......")

    


if __name__ == "__main__":
    access_court_auction_site("https://www.courtauction.go.kr/")
    # access_court_auction_site("GW_Study/Crawling/Court_auction/mainFrame_test.html")
