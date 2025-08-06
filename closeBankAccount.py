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
계좌의 정액제 해지를 요청합니다.
https://developers.popbill.com/reference/easyfinbank/python/api/manage#CloseBankAccount
"""

try:
    print("=" * 15 + " 계좌 정액제 해지신청 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 기관코드
    BankCode = ""

    # 계좌번호 하이픈('-') 제외
    AccountNumber = ""

    # 해지유형, "일반"
    # - 일반(일반해지) - 해지 요청일이 포함된 정액제 이용기간 만료 후 해지
    CloseType = "일반"

    result = easyFinBankService.closeBankAccount(
        CorpNum, BankCode, AccountNumber, CloseType
    )

    print("처리결과 : [%d] %s" % (result.code, result.message))
except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
