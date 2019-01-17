from bs4 import BeautifulSoup
import requests
import json

## 먼저 매각결과검색 html을 가지고 오는 것부터 하자.

def query2jquery(param_sources):
    ps = param_sources.split('&')
    result = {}
    for p in ps:
        pp = p.split('=')
        result[pp[0]] = pp[1]
    return result


search_url = "https://www.courtauction.go.kr/InitMulSrch.laf"   #POST

header = { "Host": "www.courtauction.go.kr",
"Origin": "https://www.courtauction.go.kr",
"Referer": "https://www.courtauction.go.kr/RetrieveMainInfo.laf",
"Upgrade-Insecure-Requests": "1",
"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36" }

param_sources = "_NAVI_CMD=&_NAVI_SRNID=&_SRCH_SRNID=PNO102000&_CUR_CMD=RetrieveMainInfo.laf&_CUR_SRNID=PNO102000&_NEXT_CMD=InitMulSrch.laf&_NEXT_SRNID=PNO102027&_PRE_SRNID=&_LOGOUT_CHK=&_FORM_YN=N"
params = query2jquery(param_sources)

session = requests.session()

response_html = session.post(search_url, headers=header)

with open('./response_html.html', mode='w', encoding='utf-8') as file:
    file.write(response_html.text)