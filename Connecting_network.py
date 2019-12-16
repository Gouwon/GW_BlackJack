import requests, time, sys
from selenium import webdriver


def do_connect():
    print(".............. SK 와이파이에 접속 중입니다.")
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument("disable-gpu")
    options.add_argument("lang=ko_KR")
    driver = webdriver.Chrome("chromedriver")
    driver.get('https://www.tfreewifi.com/wifi.do/')
    time.sleep(5)
    
    print(".............. SK 와이파이로부터 인증 중입니다.")
    try:
        driver.find_element_by_class_name('btn__confirm').click()
        time.sleep(3)
        print(".............. SK 와이파이로부터 인증이 완료되었습니다.")
    except Exception as drivererr:
        print(".............. 셀레니움 크롬드라이버(Chromedriver)에서 오류가 발생하였습니다.")
        print(">>>>>>>> drivererr message ", drivererr)
    
    time.sleep(8)
    driver.quit()

def check_connect():
    print(".............. 구글(https://www.google.com/)에 요청을 보내 연결을 확인합니다.")
    try:
        req = requests.get('https://www.google.com/', timeout=(10, 10))
        print(".............. 인터넷 연결에 문제가 없습니다.")
    except Exception as err:
        print(".............. 인터넷 연결에 오류가 발생하였습니다.")
        print(">>>>>>>> error message ", err)
        try:
            do_connect()
        except Exception as second_err:
            print(".............. 인터넷 연결 도중 오류가 발생하였습니다.")
            print(">>>>>>>> error message ", second_err)
            pass
    
    time.sleep(1)
    print(".............. 인터넷 연결 프로그램을 종료합니다. ")


check_connect()