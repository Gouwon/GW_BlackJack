import requests
import json
import Crawling_utils as cu

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
## 자동차 리스트 2Page부터는 PNIPassMsg는 불필요하다고 생각됨으로 cookie에서 삭제하고, targetRow만 21, 41, 61로 변경하도록 loop를 돌리자.

cookies2 = "page=default20&jiwonNm=%C0%FC%C3%BC&mulStatcd=0001302&mgakAmtGuganMax=&_NEXT_CMD=&realVowel=35207_45207&bubwLocGubun=1&daepyoSiguCd=&PNIPassMsg=%C1%A4%C3%A5%BF%A1+%C0%C7%C7%D8+%C2%F7%B4%DC%B5%C8+%C7%D8%BF%DCIP+%BB%E7%BF%EB%C0%DA%C0%D4%B4%CF%B4%D9.&_CUR_SRNID=PNO102027&sclsUtilCd=00008030101&daepyoDongCd=&pageSpec=default20&pageSpec=default20&_PRE_SRNID=&_SRCH_SRNID=PNO102027&gamEvalAmtGuganMax=&mclsUtilCd=000080301&_LOGOUT_CHK=&yuchalCntGuganMax=&gamEvalAmtGuganMin=&rd3Rd4Cd=&_FORM_YN=Y&daepyoSidoCd=&page=default20&_NAVI_SRNID=&_NAVI_CMD=&srnID=PNO102027&mgakAmtGuganMin=&_NEXT_SRNID=PNO102028&lclsUtilCd=0000803&jpDeptCd=000000&yuchalCntGuganMin=&_CUR_CMD=InitMulSrch.laf&rd1Cd=&rd2Cd=&targetRow=21&lafjOrderBy="
params2 = cu.cookie_parser(cookies2)

html1 = requests.post(target_url, params=params2, headers=headers).text
saveFile = './Crawling/results/result1.html'
with open(saveFile, 'w', encoding='utf-8') as file:
    file.write(html1)

print("______전국 자동차 매각 결과 리스트 2PAGE HTML 저장 완료 ______")
