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
계좌조회 정액제 서비스 상태를 확인합니다.
- https://developers.popbill.com/reference/easyfinbank/python/api/point#GetFlatRateState
"""

try:
    print("=" * 15 + " 정액제 서비스 상태 확인 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 기관코드
    BankCode = ""

    # 계좌번호
    AccountNumber = ""

    response = easyFinBankService.getFlatRateState(CorpNum, BankCode, AccountNumber)

    print("referenceID (계좌아아디) : %s" % response.referenceID)
    print("contractDT (정액제 서비스 시작일시) : %s" % response.contractDT)
    print("useEndDate (정액제 서비스 종료일자) : %s" % response.useEndDate)
    print("baseDate (자동연장 결제일) : %s" % response.baseDate)
    print("state (정액제 서비스 상태 [1-사용, 2-해지]) : %s" % response.state)
    print("closeRequestYN (정액제 서비스 해지신청 여부) : %s" % response.closeRequestYN)
    print("useRestrictYN (정액세 서비스 사용제한 여부) : %s" % response.useRestrictYN)
    print("closeOnExpired (정액제 서비스 만료 시 해지 여부) : %s" % response.closeOnExpired)
    print("unPaidYN (미수금 보유 여부): %s" % response.unPaidYN)

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
