## 셀레니움으로 접근하여 지원 번호 수집.

def access_court_auction_site(url):
    from selenium import webdriver
    from selenium.webdriver.support.ui import Select
    import os
    

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

    driver.switch_to.frame(driver.find_elements_by_tag_name("frame")[0])

    ## 법원경매 매각결과검색 페이지 접속
    driver.execute_script( open('../jquery-3.3.1.js').read() )
    driver.execute_script("$('#menu_s_2_son > div.son_h > ul > li:nth-child(8) > a').click();")
    driver.implicitly_wait(20)

    ## 법원경매 매각결과검색 설정
    handles2 = len(driver.window_handles)
    print(">>>>>>>>>>", handles2)

    # driver.switch_to.frame(driver.find_elements_by_tag_name("frame")[0])
    userinput = input(">>>>>>>>>>>")

    
    driver.execute_script( open('../jquery-3.3.1.js').read() )
    driver.execute_script("$('#idJiwonNm > [value='전체']').click();")
    driver.execute_script("$('#idMulStatcd > option:nth-child(2)').click();")   # { '매각' : '0001302' , '유찰' : '0001301', '전체' : ''}
    driver.execute_script("$('#idLevel1 > option:nth-child(4)').click();")  # {'차량및운송장비' : '0000803' , '건물' : '0000802'}
    # driver.execute_script("$('#idLevel2').value = '000080301';") # 차량
    # driver.execute_script("$('#idLevel3').value = '00008030101';")
    search_page_source = driver.page_source #search_page_source는 str
    
    print(">>>>>>>>>>>>>", type(search_page_source))

    # with open('./search_page_source.html', mode='w', encoding='utf-8') as file:
    #     file.write(search_page_source)

    # from bs4 import BeautifulSoup

    # soup = BeautifulSoup(search_page_source, 'html.parser')
    driver.find_element_by_xpath('//*[@id="idLevel1"]/option[4]').click()
    userinput = input(">>>>>>>>>>>")

    driver.execute_script("$('#contents > form > div > a:nth-child(1)').click();")

    userinput = input(">>>>>>>>>>>")
    # driver.execute_script("$('#idLevel1').value = '전체';")


    print("00000")
    # response_indexFrame = driver.find_elements_by_tag_name('frame').indexFrame

    # print(html)
    driver.close()


if __name__ == "__main__":
    access_court_auction_site("https://www.courtauction.go.kr/")
    # access_court_auction_site("GW_Study/Crawling/Court_auction/mainFrame_test.html")
