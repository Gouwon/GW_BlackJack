import requests
import json
import Crawling_utils as cu
from bs4 import BeautifulSoup
import urllib

detail_request_url = "https://www.courtauction.go.kr/RetrieveRealEstDetailInqSaList.laf"

headers = {'Referer': 'https://www.courtauction.go.kr/RetrieveRealEstMgakGyulgwaMulList.laf',
           "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}

params = {'jiwonNm':'%BC%AD%BF%EF%C1%DF%BE%D3%C1%F6%B9%E6%B9%FD%BF%F8',
'saNo':'20180130105447',
'maemulSer':'',
'mokmulSer':'',
'isSessionless':'',
'_NAVI_CMD':'InitMulSrch.laf',
'_NAVI_SRNID':'PNO102027',
'_SRCH_SRNID':'PNO102027',
'_CUR_CMD':'RetrieveRealEstMgakGyulgwaMulList.laf',
'_CUR_SRNID':'PNO102028',
'_NEXT_CMD':'RetrieveRealEstDetailInqSaList.laf',
'_NEXT_SRNID':'PNO102018',
'_PRE_SRNID':'',
'_LOGOUT_CHK':'',
'_FORM_YN':'Y',
'_C_jiwonNm':'%C0%FC%C3%BC',
'_C_mulStatcd':'0001302',
'_C_mgakAmtGuganMax':'',
'_C_realVowel':'35207_45207',
'_C_daepyoSiguCd':'',
'_C_gamEvalAmtGuganMin':'',
'_C_sclsUtilCd':'00008030101',
'_C_daepyoDongCd':'',
'_C_gamEvalAmtGuganMax':'',
'_C_mclsUtilCd':'000080301',
'_C_yuchalCntGuganMax':'',
'_C_rd3Rd4Cd':'',
'_C_daepyoSidoCd':'',
'_C_bubwLocGubun':'1',
'_C_srnID':'PNO102027',
'_C_mgakAmtGuganMin':'',
'_C_lclsUtilCd':'0000803',
'_C_jpDeptCd':'000000',
'_C_yuchalCntGuganMin':'',
'_C_rd1Cd':'',
'_C_rd2Cd':''}

cookies_detail = 'jiwonNm=&saNo=&maemulSer=&mokmulSer=&isSessionless=&_NAVI_CMD=InitMulSrch.laf&_NAVI_SRNID=PNO102027&_SRCH_SRNID=PNO102027&_CUR_CMD=RetrieveRealEstMgakGyulgwaMulList.laf&_CUR_SRNID=PNO102028&_NEXT_CMD=RetrieveRealEstDetailInqSaList.laf&_NEXT_SRNID=PNO102018&_PRE_SRNID=&_LOGOUT_CHK=&_FORM_YN=Y&_C_jiwonNm=%C0%FC%C3%BC&_C_mulStatcd=0001302&_C_mgakAmtGuganMax=&_C_realVowel=35207_45207&_C_daepyoSiguCd=&_C_gamEvalAmtGuganMin=&_C_sclsUtilCd=00008030101&_C_daepyoDongCd=&_C_gamEvalAmtGuganMax=&_C_mclsUtilCd=000080301&_C_yuchalCntGuganMax=&_C_rd3Rd4Cd=&_C_daepyoSidoCd=&_C_bubwLocGubun=1&_C_srnID=PNO102027&_C_mgakAmtGuganMin=&_C_lclsUtilCd=0000803&_C_jpDeptCd=000000&_C_yuchalCntGuganMin=&_C_rd1Cd=&_C_rd2Cd='





# params_detail = cu.cookie_parser(cookies_detail)


# p=urllib.parse.quote_plus('서울중앙지방법원')
# ## %BC%AD%BF%EF%C1%DF%BE%D3%C1%F6%B9%E6%B9%FD%BF%F8
# # print(p)
# # params_detail['jiwonNm'] = p
# params_detail['jiwonNm'] =  '서울중앙지방법원'
# # params_detail['jiwonNm'] = '%BC%AD%BF%EF%C1%DF%BE%D3%C1%F6%B9%E6%B9%FD%BF%F8'

# sss = '%BC%AD%BF%EF%C1%DF%BE%D3%C1%F6%B9%E6%B9%FD%BF%F8'
# print(">>>>>>>>>>>", urllib.parse.unquote(sss))


# # print(type(p))
# # params_detail['saNo'] = '20170130015297'
# params_detail['saNo'] = '20180130105447'
# print(params_detail)

# aaa = "%EC%84%9C%EC%9A%B8%EC%A4%91%EC%95%99%EC%A7%80%EB%B0%A9%EB%B2%95%EC%9B%90"
# aaa = '%BA%CE%C3%B5%C1%F6%BF%F8&'
# print(urllib.parse.unquote(aaa))

# # exit()
result = requests.post(detail_request_url, params=params, headers=headers)
print("::>>", result.url)
html1 = result.text
saveFile = './Crawling/results/result____test.html'
with open(saveFile, 'w', encoding='utf-8') as file:
    file.write(html1)

# p = [ '서울중앙지방법원', '서울동부지방법원', '서울서부지방법원', '서울남부지방법원', '서울북부지방법원', '의정부지방법원', '고양지원', '인천지방법원', '부천지원', '수원지방법원', '성남지원', '여주지원', '평택지원', '안산지원', '안양지원', '춘천지방법원', '강릉지원', '원주지원', '속초지원', '영월지원', '청주지방법원', '충주지원', '제천지원', '영동지원', '대전지방법원', '홍성지원', '논산지원', '천안지원', '공주지원', '서산지원', '대구지방법원', '안동지원', '경주지원', '김천지원', '상주지원', '의성지원', '영덕지원', '포항지원', '대구서부지원', '부산지방법원', '부산동부지원', '부산서부지원', '울산지방법원', '창원지방법원', '마산지원', '진주지원', '통영지원', '밀양지원', '거창지원', '광주지방법원', '목포지원', '장흥지원', '순천지원', '해남지원', '전주지방법원', '군산지원', '정읍지원', '남원지원', '제주지방법원', '전체' ]

# dd = {}
# for i in p:
#     dd[i] = urllib.parse.quote_plus(i)

# sd = urllib.parse.quote_plus('%BA%CE%C3%B5%C1%F6%BF%F8&')
# print(sd)
# print(dd)
# for i in dd:
#     if dd[i] == '%BA%CE%C3%B5%C1%F6%BF%F8&':
#         print(i)
#     else:
#         continue