from bs4 import BeautifulSoup
import requests
import json
import time

url = "http://rt.molit.go.kr/new/gis/getDongListAjax.do" #POST

params = {
    'menuGubun': 'A' ,
    'gubunCode': 'LAND',
    'sidoCode': '11',
    'gugunCode': '11350'
}

headers = {
   'Referer': 'http://rt.molit.go.kr/new/gis/srh.do?menuGubun=A&gubunCode=LAND',
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}

html = requests.post(url, params=params, headers=headers).text

jsonData = json.loads(html)
dongCode = {}


for gu in jsonData["jsonList"]:
    dongCode[gu['NAME']] = gu['CODE']

############################## 동코드 완료.
headers = {
'Referer': 'http://rt.molit.go.kr/new/gis/srh.do?menuGubun=A&gubunCode=LAND',
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}

for i, j in enumerate(dongCode):    ## 동코드 loop 
 
    url = "http://rt.molit.go.kr/new/gis/getDanjiComboAjax.do" #POST
    params = {
        'menuGubun': 'A',
        'srhYear': '2019',
        'srhLastYear': '2018',
        'gubunCode': 'LAND',
        'sidoCode': '11',
        'gugunCode': '11350',
        'dongCode': str(dongCode[j]),
        'rentAmtType': '3'
    }

    html = requests.post(url, params=params, headers=headers).text
    jsonData = json.loads(html)
    APT_CODE = {}
   
    for APT in jsonData["jsonList"]:
        APT_CODE[APT['APT_NAME']] = APT['APT_CODE']
    ############################# 아파트코드 완료
    print(">>>>>>>>>>>>>>",APT_CODE)

    url = "http://rt.molit.go.kr/new/gis/getDanjiInfoDetail.do?menuGubun=A&p_apt_code=52683&p_house_cd=1&p_acc_year=2018&areaCode=&priceCode=" 
    #GET

    headers = {
    'Referer': 'http://rt.molit.go.kr/new/gis/srh.do?menuGubun=A&gubunCode=LAND',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
    }

    for i, j in enumerate(APT_CODE):
        
        params = {
            'menuGubun': 'A',
            'p_apt_code': "'"+str(APT_CODE[j])+"'",
            'p_house_cd': '1',
            'p_acc_year': '2018'
        }
        
        html = requests.get(url, params=params, headers=headers).text
        jsonData = json.loads(html)
        # print(params['p_apt_code'])
        print(html)
        # APT_FINAL_INFOS = []

        for APT_FINAL_INFO in jsonData["result"]:
            # print(APT_FINAL_INFO)
            # continue
            FINAL = {APT_FINAL_INFO["BLDG_CD"] : 
                {
                    "DNAME"   : APT_FINAL_INFO["DNAME"],
                    "BLDG_NM": APT_FINAL_INFO["BLDG_NM"],
                    "BOBN": APT_FINAL_INFO["BOBN"],
                    "BLDG_AREA": APT_FINAL_INFO["BLDG_AREA"],
                    "DEAL_MM": APT_FINAL_INFO["DEAL_MM"],
                    "DEAL_DD": APT_FINAL_INFO["DEAL_DD"],
                    "SUM_AMT": APT_FINAL_INFO["SUM_AMT"],
                    "APTFNO": APT_FINAL_INFO["APTFNO"],
                    "BUILD_YEAR": APT_FINAL_INFO["BUILD_YEAR"],
                    "ROAD_LEN": APT_FINAL_INFO["ROAD_LEN"],
                    "BC_RAT": APT_FINAL_INFO["BC_RAT"],
                    "VL_RAT": APT_FINAL_INFO["VL_RAT"]
                }
            }
            # time.sleep(1)
            # print(FINAL)    

            with open("./hello/scraping/results/results_house.html", mode="a") as file:
                file.write(str(FINAL))
    
# BLDG_CD: 20332148
# DNAME: "공릉동"
# BLDG_NM: "670-7"
# BOBN: "670-7"
# BLDG_AREA: 17.27
# DEAL_MM: "10"
# DEAL_DD: "11~20"
# SUM_AMT: "17,400"
# APTFNO: 12
# BUILD_YEAR: 2016
# ROAD_LEN: "25m이상"
# BC_RAT: "56~60%"
# VL_RAT: "626~630%"


# HO_CODE: 53
# LAND_USE_LAW: "[포함]학교환경위생정화구역<학교보건법>(공릉초. 최종확인은 관할교육청에 반드시 문의),[포함]학교환경위생정화구역<학교보건법>(최종확인은관할교육청에반드시확인),[포함]대공방어협조구역<군사기지 및 군사시설보호법>(위탁고도:77-257m),[포함]가축사육제한구역<가축분뇨의관리및이용에관한법률>,[포함]한강폐기물매립시설설치제한지역<한강수계상수원수질개선및주민지원등에관한법률>(자세한사항은 자원순환과로 문의),[포함]과밀억제권역<수도권정비계획법>"
# LAND_USE_NM: "[포함]도시지역,[포함]일반상업지역,[포함]제1종지구단위계획구역,[접합]제3종일반주거지역,[접합]도로"
# BLDG_CD: 20332148
# DONG_CODE: 1
# ETC_STRCT: "철근콘크리트구조"
# GRND_FLR_CNT: "-"
# JIBUN_NAME: "서울특별시 노원구  공릉동"
# LAND_MOVE1: "198*"
# LAND_MOVE2: "행정관할구역변경"


# 서울특별시 아파트 실거래가
# 2006년~ 2018년자료 가지고 오기

# ##### 최종정보