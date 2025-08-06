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
종량제 이용시 등록된 계좌를 삭제합니다.
- https://developers.popbill.com/reference/easyfinbank/python/api/manage#DeleteBankAccount
"""

try:
    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 기관코드
    BankCode = ""

    # 계좌번호 하이픈('-') 제외
    AccountNumber = ""

    response = easyFinBankService.deleteBankAccount(CorpNum, BankCode, AccountNumber)

    print("처리결과 : [%d] %s" % (result.code, result.message))
except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
