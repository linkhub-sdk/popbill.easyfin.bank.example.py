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
파트너 포인트 충전 팝업 URL을 반환합니다.
- 보안정책에 따라 반환된 URL은 30초의 유효시간을 갖습니다.
- https://docs.popbill.com/easyfinbank/python/api#GetPartnerURL
'''

try:
    print("=" * 15 + " 파트너 포인트충전 팝업 URL 확인 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # CHRG-포인트 충전 URL
    TOGO = "CHRG"

    url = easyFinBankService.getPartnerURL(CorpNum, TOGO)

    print("URL : %s" % url)

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
