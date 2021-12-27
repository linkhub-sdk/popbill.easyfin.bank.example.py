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
easyFinBankService.UseLocalTimeYN = testValue.UseLocalTimeYN

'''
계좌 거래내역 수집을 요청합니다. (조회기간 단위 : 최대 1개월)
- 조회일로부터 최대 3개월 이전 내역까지 조회할 수 있습니다.
- 수집 요청후 반환받은 작업아이디(JobID)의 유효시간은 1시간 입니다.
- https://docs.popbill.com/easyfinbank/python/api#RequestJob
'''

try:
    print("=" * 15 + " 수집 요청 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 팝빌회원 아이디
    UserID = testValue.testUserID

    # 기관코드
    BankCode = "0039"

    # 계좌번호
    AccountNumber = "2070064402404"

    # 시작일자, 날짜형식(yyyyMMdd)
    SDate = "20211201"

    # 종료일자, 날짜형식(yyyyMMdd)
    EDate = "20211230"

    jobID = easyFinBankService.requestJob(CorpNum, BankCode, AccountNumber, SDate, EDate, UserID)

    print("작업아이디(jobID) : " + jobID)

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code , PE.message))
