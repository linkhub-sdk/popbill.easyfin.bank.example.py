# -*- coding: utf-8 -*-
# code for console Encoding difference. Dont' mind on it
import imp
import sys

from popbill import EasyFinBankService, PopbillException

import testValue

imp.reload(sys)
try:
    sys.setdefaultencoding("UTF8")
except Exception as E:
    pass

easyFinBankService = EasyFinBankService(testValue.LinkID, testValue.SecretKey)
easyFinBankService.IsTest = testValue.IsTest
easyFinBankService.IPRestrictOnOff = testValue.IPRestrictOnOff
easyFinBankService.UseStaticIP = testValue.UseStaticIP
easyFinBankService.UseLocalTimeYN = testValue.UseLocalTimeYN

"""
계좌 거래내역을 확인하기 위해 팝빌에 수집요청을 합니다. (조회기간 단위 : 최대 1개월)
- 조회일로부터 최대 3개월 이전 내역까지 조회할 수 있습니다.
- 반환 받은 작업아이디는 함수 호출 시점부터 1시간 동안 유효합니다.
- https://developers.popbill.com/reference/easyfinbank/python/api/job#RequestJob
"""

try:
    print("=" * 15 + " 수집 요청 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 기관코드
    BankCode = ""

    # 계좌번호
    AccountNumber = ""

    # 시작일자, 날짜형식(yyyyMMdd)
    SDate = "20220701"

    # 종료일자, 날짜형식(yyyyMMdd)
    EDate = "20220731"

    jobID = easyFinBankService.requestJob(
        CorpNum, BankCode, AccountNumber, SDate, EDate
    )

    print("작업아이디(jobID) : " + jobID)

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
