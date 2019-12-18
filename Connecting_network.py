import requests, time, sys
from selenium import webdriver


def do_connect():
    print(".................. SK 와이파이에 접속 중입니다.")
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument("disable-gpu")
    options.add_argument("lang=ko_KR")
    driver = webdriver.Chrome("chromedriver")
    driver.get('https://www.tfreewifi.com/wifi.do/')
    time.sleep(5)
    print(".................. SK 와이파이로부터 인증 중입니다.")
    try:
        driver.implicitly_wait(4)
        driver.find_element_by_class_name('btn__confirm').click()
        time.sleep(5)
        print(".................. SK 와이파이로부터 인증이 완료되었습니다.")
    except Exception as drivererr:
        print(".................. 셀레니움 크롬드라이버(Chromedriver)에서 오류가 발생하였습니다.")
        print(">>>>>>>> drivererr message ", drivererr)
    finally:
        driver.quit()
    
    time.sleep(5)
    driver.quit()

def check_connect():
    try:
        print(".................. 인터넷 연결 프로그램을 시작합니다.")
        do_connect()
    except Exception as err:
        print(".................. 인터넷 연결 도중 오류가 발생하였습니다.")
        print(">>>>>>>> error message ", err)
    finally:
        time.sleep(1)
        print(".................. 인터넷 연결 프로그램을 종료합니다.")

check_connect()