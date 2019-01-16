## 먼저 셀레니움으로 법원을 이름으로 접근하여서, 법원에 따른 실제 url param의 jiwonNm을 알아내는 프로그램을 만들어보자.

import requests
import json
import Crawling_utils as cu
from bs4 import BeautifulSoup

target_url = "https://www.courtauction.go.kr/RetrieveRealEstMgakGyulgwaMulList.laf"


headers = {'Referer': 'https://www.courtauction.go.kr/InitMulSrch.laf',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}

cookies = 'bubwLocGubun=1&jiwonNm=%C0%FC%C3%BC&jpDeptCd=000000&daepyoSidoCd=&daepyoSiguCd=&daepyoDongCd=&rd1Cd=&rd2Cd=&realVowel=35207_45207&rd3Rd4Cd=&mgakAmtGuganMin=&mgakAmtGuganMax=&gamEvalAmtGuganMin=&gamEvalAmtGuganMax=&mulStatcd=0001302&yuchalCntGuganMin=&yuchalCntGuganMax=&lclsUtilCd=0000803&mclsUtilCd=000080301&sclsUtilCd=00008030101&srnID=PNO102027&_NAVI_CMD=&_NAVI_SRNID=&_SRCH_SRNID=PNO102027&_CUR_CMD=InitMulSrch.laf&_CUR_SRNID=PNO102027&_NEXT_CMD=RetrieveRealEstMgakGyulgwaMulList.laf&_NEXT_SRNID=PNO102028&_PRE_SRNID=&_LOGOUT_CHK=&_FORM_YN=Y'
params = cu.cookie_parser(cookies)

html = requests.post(target_url, params=params, headers=headers).text
saveFile = './Crawling/results/result.html'
with open(saveFile, 'w', encoding='utf-8') as file:
    file.write(html)

print("______전국 자동차 매각 결과 리스트 1PAGE HTML 저장 완료 ______")
## 전체 리스트를 가지고 오려면 target_url로 다음의 쿠키를 이용하여 반복해서 html 파일을 만들어서 저장하고, 읽어들여서 별도의 파일에 자동차 목록만 일단 저장하자.

## 1Page에서 Parsing하여 [총 물건수]에 있는 content를 뽑아야지 아래의 targetRow 돌릴 수 있다.
soup = BeautifulSoup(html, 'html.parser')
selector = "#search_title li.txtblue"
case_cnt_tag = soup.select_one(selector).text
# print(case_cnt_tag[r"^\:.건"])
print(case_cnt_tag)
print(type(case_cnt_tag))
import re
pattern = re.compile("\:(.*)건")
case_cnt = re.findall(pattern, case_cnt_tag)

import math
total_targetRow = math.ceil(int(case_cnt[0]) / 20)

for i in range(0,total_targetRow):
    if i == 0:
        continue
    targetRow = 1 + (20 * i)
    print(targetRow, type(targetRow))
# exit()
## 자동차 리스트 2Page부터는 PNIPassMsg는 불필요하다고 생각됨으로 cookie에서 삭제하고, targetRow만 21, 41, 61로 변경하도록 loop를 돌리자.

    cookies2 = "page=default20&jiwonNm=%C0%FC%C3%BC&mulStatcd=0001302&mgakAmtGuganMax=&_NEXT_CMD=&realVowel=35207_45207&bubwLocGubun=1&daepyoSiguCd=&PNIPassMsg=%C1%A4%C3%A5%BF%A1+%C0%C7%C7%D8+%C2%F7%B4%DC%B5%C8+%C7%D8%BF%DCIP+%BB%E7%BF%EB%C0%DA%C0%D4%B4%CF%B4%D9.&_CUR_SRNID=PNO102027&sclsUtilCd=00008030101&daepyoDongCd=&pageSpec=default20&pageSpec=default20&_PRE_SRNID=&_SRCH_SRNID=PNO102027&gamEvalAmtGuganMax=&mclsUtilCd=000080301&_LOGOUT_CHK=&yuchalCntGuganMax=&gamEvalAmtGuganMin=&rd3Rd4Cd=&_FORM_YN=Y&daepyoSidoCd=&page=default20&_NAVI_SRNID=&_NAVI_CMD=&srnID=PNO102027&mgakAmtGuganMin=&_NEXT_SRNID=PNO102028&lclsUtilCd=0000803&jpDeptCd=000000&yuchalCntGuganMin=&_CUR_CMD=InitMulSrch.laf&rd1Cd=&rd2Cd=&targetRow=&lafjOrderBy="
    params2 = cu.cookie_parser(cookies2)

    params2['targetRow'] = str(targetRow)

    html1 = requests.post(target_url, params=params2, headers=headers).text
    saveFile = './Crawling/results/result{}.html'.format(i)
    with open(saveFile, 'w', encoding='utf-8') as file:
        file.write(html1)

    print("______전국 자동차 매각 결과 리스트 {}PAGE HTML 저장 완료 ______".format(i+1))

## 전체 자동차 매각 결과 리스트 html 파일 저장 완료

## 이제 읽어 들인 것에서 상세 페이지로 Request 보내서 저장해야 함.
## 읽어 들인 것에서 법원과 사건번호.....
 

detail_request_url = "https://www.courtauction.go.kr/RetrieveRealEstDetailInqSaList.laf#"

headers = {"referer":"https://www.courtauction.go.kr/RetrieveRealEstMgakGyulgwaMulList.laf#",
           "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}

cookies_detail = "jiwonNm=%BC%AD%BF%EF%C1%DF%BE%D3%C1%F6%B9%E6%B9%FD%BF%F8&saNo=20180130006083&maemulSer=&mokmulSer=&isSessionless=&_NAVI_CMD=InitMulSrch.laf&_NAVI_SRNID=PNO102027&_SRCH_SRNID=PNO102027&_CUR_CMD=RetrieveRealEstMgakGyulgwaMulList.laf&_CUR_SRNID=PNO102028&_NEXT_CMD=RetrieveRealEstDetailInqSaList.laf&_NEXT_SRNID=PNO102018&_PRE_SRNID=&_LOGOUT_CHK=&_FORM_YN=Y&_C_jiwonNm=%C0%FC%C3%BC&_C_mulStatcd=0001302&_C_mgakAmtGuganMax=&_C_realVowel=35207_45207&_C_daepyoSiguCd=&_C_gamEvalAmtGuganMin=&_C_sclsUtilCd=00008030101&_C_daepyoDongCd=&_C_gamEvalAmtGuganMax=&_C_mclsUtilCd=000080301&_C_yuchalCntGuganMax=&_C_rd3Rd4Cd=&_C_daepyoSidoCd=&_C_bubwLocGubun=1&_C_srnID=PNO102027&_C_mgakAmtGuganMin=&_C_lclsUtilCd=0000803&_C_jpDeptCd=000000&_C_yuchalCntGuganMin=&_C_rd1Cd=&_C_rd2Cd="
params_detail = cu.cookie_parser(cookies_detail)

html1 = requests.post(target_url, params=params2, headers=headers).text
saveFile = './Crawling/results/result{}.html'.format(i)
with open(saveFile, 'w', encoding='utf-8') as file:
    file.write(html1)


import urllib
# p= urllib.unquote(params_detail['jiwonNm'],)
p = urllib.parse.quote_plus(params_detail['jiwonNm'], safe='', encoding=None, errors=None)
print(p)
# import urllib
# urllib.unquote()
# urllib.quote()