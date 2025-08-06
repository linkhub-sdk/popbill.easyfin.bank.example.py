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
계좌조회 API 연동서비스 과금정보를 확인합니다.
- https://developers.popbill.com/reference/easyfinbank/python/common-api/point#GetChargeInfo
"""

try:
    print("=" * 15 + " 과금정보 확인 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    response = easyFinBankService.getChargeInfo(CorpNum)

    print(" unitCost (월정액요금) : %s" % response.unitCost)
    print(" chargeMethod (과금유형) : %s" % response.chargeMethod)
    print(" rateSystem (과금제도) : %s" % response.rateSystem)

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
