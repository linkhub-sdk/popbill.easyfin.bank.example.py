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


'''
계좌 거래내역 수집을 요청합니다
- 수집 요청후 반환받은 작업아이디(JobID)의 유효시간은 1시간 입니다.
'''

try:
    print("=" * 15 + " 수집 요청 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 팝빌회원 아이디
    UserID = testValue.testUserID

    # 은행코드
    BankCode = "0048"

    # 계좌번호
    AccountNumber = "131020538645"

    # 시작일자, 날짜형식(yyyyMMdd)
    SDate = "20191004"

    # 종료일자, 날짜형식(yyyyMMdd)
    EDate = "20200102"

    jobID = easyFinBankService.requestJob(CorpNum, BankCode, AccountNumber, SDate, EDate, UserID)

    print("작업아이디(jobID) : " + jobID)

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code , PE.message))
