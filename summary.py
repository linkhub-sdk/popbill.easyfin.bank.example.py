# -*- coding: utf-8 -*-
# code for console Encoding difference. Dont' mind on it
import sys
import imp
import testValue

from popbill import EasyFinBankService, PopbillException

imp.reload(sys)
try:
    sys.setdefaultencoding('UTF8')
except Exception as E:
    pass

easyFinBankService = EasyFinBankService(testValue.LinkID, testValue.SecretKey)
easyFinBankService.IsTest = testValue.IsTest
easyFinBankService.IPRestrictOnOff = testValue.IPRestrictOnOff
easyFinBankService.UseStaticIP = testValue.UseStaticIP

'''
검색조건을 사용하여 수집 결과 요약정보를 조회합니다.
- https://docs.popbill.com/easyfinbank/python/api#Summary
'''

try:
    print("=" * 15 + "수집 결과 요약정보 조회 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 팝빌회원 아이디
    UserID = testValue.testUserID

    # 수집요청(requestJob)시 발급받은 작업아이디
    JobID = "020010214000000014"

    # 거래유형 배열, I - 입금 / O - 출금
    TradeType = ["I", "O"]

    # 조회 검색어 - 입금/출금액, 메모, 적요 like 검색 가능
    SearchString = ""

    response = easyFinBankService.summary(CorpNum, JobID, TradeType, SearchString, UserID)


    print("count (수집 결과 건수) : %s " % response.count)
    print("cntAccIn (입금거래 건수) : %s " % response.cntAccIn)
    print("cntAccOut (출금거래 건수) : %s " % response.cntAccOut)
    print("totalAccIn (입금액 합계) : %s " % response.totalAccIn)
    print("totalAccOut (출금액 합계) : %s " % response.totalAccOut)

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
