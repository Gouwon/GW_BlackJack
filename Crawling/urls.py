import os
import urllib.parse as parse
import os.path as path

def getFilename(url):
    p = parse.urlparse(url).path
    return path.basename(p)

def getHostname(url, withProtocol=False):
    p = parse.urlparse(url)
    if withProtocol:
        return "{}://{}".format(p.scheme, p.hostname)
    else:
        return p.hostname

def urljoin(url, p):
    return parse.urljoin(url, p)

def q2j(s):
    ps = s.split('&')
    for p in ps:
        pp = p.split('=')
        print("'{}':'{}',".format(pp[0], pp[1]))

if __name__ == '__main__':
    str = "jiwonNm=%BC%AD%BF%EF%C1%DF%BE%D3%C1%F6%B9%E6%B9%FD%BF%F8&saNo=20180130105447&maemulSer=&mokmulSer=&isSessionless=&_NAVI_CMD=InitMulSrch.laf&_NAVI_SRNID=PNO102027&_SRCH_SRNID=PNO102027&_CUR_CMD=RetrieveRealEstMgakGyulgwaMulList.laf&_CUR_SRNID=PNO102028&_NEXT_CMD=RetrieveRealEstDetailInqSaList.laf&_NEXT_SRNID=PNO102018&_PRE_SRNID=&_LOGOUT_CHK=&_FORM_YN=Y&_C_jiwonNm=%C0%FC%C3%BC&_C_mulStatcd=0001302&_C_mgakAmtGuganMax=&_C_realVowel=35207_45207&_C_daepyoSiguCd=&_C_gamEvalAmtGuganMin=&_C_sclsUtilCd=00008030101&_C_daepyoDongCd=&_C_gamEvalAmtGuganMax=&_C_mclsUtilCd=000080301&_C_yuchalCntGuganMax=&_C_rd3Rd4Cd=&_C_daepyoSidoCd=&_C_bubwLocGubun=1&_C_srnID=PNO102027&_C_mgakAmtGuganMin=&_C_lclsUtilCd=0000803&_C_jpDeptCd=000000&_C_yuchalCntGuganMin=&_C_rd1Cd=&_C_rd2Cd="
    q2j(str)


    # print(os.name)

    # url = "https://blog.naver.com/jeonseongho/1212.jpg"
    # print("filename=", getFilename(url))
    # print("hostname=", getHostname(url))
    # print("URL=", getHostname(url, True))
    # print("QQ>>", urljoin("https://nave.com", "bbb.jpg?aaaa=1"))
