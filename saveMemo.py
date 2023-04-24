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
한 건의 거래 내역에 메모를 저장합니다.
- https://developers.popbill.com/reference/easyfinbank/python/api/search#SaveMemo
"""

try:
    print("=" * 15 + " 거래내역 메모 저장 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 거래내역 아이디
    TID = "02208021500000000120220720000004"

    # 메모
    Memo = "PYTHON 메모 테스트"

    result = easyFinBankService.saveMemo(CorpNum, TID, Memo)

    print("처리결과 : [%d] %s" % (result.code, result.message))
except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
