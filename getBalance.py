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
연동회원의 잔여포인트를 확인합니다.
- https://developers.popbill.com/reference/easyfinbank/python/api/point#GetBalance
"""

try:
    print("=" * 15 + " 연동회원 잔여포인트 확인 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    balance = easyFinBankService.getBalance(CorpNum)

    print("잔여포인트 : %f" % balance)
except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
