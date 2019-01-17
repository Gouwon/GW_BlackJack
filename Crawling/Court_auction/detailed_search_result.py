def query2jquery(param_sources):
    ps = param_sources.split('&')
    result = {}
    for p in ps:
        pp = p.split('=')
        result[pp[0]] = pp[1]
    return result

import requests
from bs4 import BeautifulSoup

request_url = "https://www.courtauction.go.kr/RetrieveRealEstDetailInqSaList.laf"

header = {'Referer': 'https://www.courtauction.go.kr/RetrieveRealEstMgakGyulgwaMulList.laf',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}

param_sources = "jiwonNm=%BC%AD%BF%EF%C1%DF%BE%D3%C1%F6%B9%E6%B9%FD%BF%F8&saNo=20180130006083&maemulSer=&mokmulSer=&isSessionless=&_NAVI_CMD=InitMulSrch.laf&_NAVI_SRNID=PNO102027&_SRCH_SRNID=PNO102027&_CUR_CMD=RetrieveRealEstMgakGyulgwaMulList.laf&_CUR_SRNID=PNO102028&_NEXT_CMD=RetrieveRealEstDetailInqSaList.laf&_NEXT_SRNID=PNO102018&_PRE_SRNID=&_LOGOUT_CHK=&_FORM_YN=Y&_C_jiwonNm=%C0%FC%C3%BC&_C_mulStatcd=0001302&_C_mgakAmtGuganMax=&_C_realVowel=35207_45207&_C_daepyoSiguCd=&_C_gamEvalAmtGuganMin=&_C_sclsUtilCd=00008030101&_C_daepyoDongCd=&_C_gamEvalAmtGuganMax=&_C_mclsUtilCd=000080301&_C_yuchalCntGuganMax=&_C_rd3Rd4Cd=&_C_daepyoSidoCd=&_C_bubwLocGubun=1&_C_srnID=PNO102027&_C_mgakAmtGuganMin=&_C_lclsUtilCd=0000803&_C_jpDeptCd=000000&_C_yuchalCntGuganMin=&_C_rd1Cd=&_C_rd2Cd="

params = query2jquery(param_sources)

session = requests.session()

response = session.post(request_url, headers=header, params=params)
print(response)

# with open('./detailed_result.html', 'w', 'utf-8') as file:
#     file.write(response.text)