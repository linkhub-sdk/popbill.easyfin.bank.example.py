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
정액제 서비스 신청 팝업 URL을 반환합니다.
- 보안정책에 따라 반환된 URL은 30초의 유효시간을 갖습니다.
'''

try:
    print("=" * 15 + " 정액제 서비스 신청 팝업 URL " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    url = easyFinBankService.getFlatRatePopUpURL(CorpNum)

    print("URL : %s" % url)

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
