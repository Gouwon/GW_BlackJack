def cookie_parser(cookies):
    result = {}
    cookie = cookies.split('&')
    for ck in cookie:
        ck_splited = ck.split('=')
        result[ck_splited[0]] = ck_splited[1]
    # print(result)
    return result

if __name__ == '__main__':
    # cookies = 'WMONID=mE3yL_WcR59; realJiwonNm=%BC%AD%BF%EF%BA%CF%BA%CE%C1%F6%B9%E6%B9%FD%BF%F8; locIdx=201801300078701; toMul=%BC%AD%BF%EF%BA%CF%BA%CE%C1%F6%B9%E6%B9%FD%BF%F8%2C20180130007870%2C1%2C20190121%2CB%5E; JSESSIONID=Dw4yc3xpTsGZVTQ2f0hqr815Lh89jhhXKhqkPJpZh2572q0mhR9L!-1994914894!145857652'

    cookies = 'bubwLocGubun=1&jiwonNm=%BC%AD%BF%EF%C1%DF%BE%D3%C1%F6%B9%E6%B9%FD%BF%F8&jpDeptCd=000000&daepyoSidoCd=&daepyoSiguCd=&daepyoDongCd=&rd1Cd=&rd2Cd=&realVowel=35207_45207&rd3Rd4Cd=&mgakAmtGuganMin=&mgakAmtGuganMax=&gamEvalAmtGuganMin=&gamEvalAmtGuganMax=&mulStatcd=0001302&yuchalCntGuganMin=&yuchalCntGuganMax=&lclsUtilCd=0000803&mclsUtilCd=000080301&sclsUtilCd=00008030101&srnID=PNO102027&_NAVI_CMD=&_NAVI_SRNID=&_SRCH_SRNID=PNO102027&_CUR_CMD=InitMulSrch.laf&_CUR_SRNID=PNO102027&_NEXT_CMD=RetrieveRealEstMgakGyulgwaMulList.laf&_NEXT_SRNID=PNO102028&_PRE_SRNID=&_LOGOUT_CHK=&_FORM_YN=Y'
    cookie_parser(cookies)