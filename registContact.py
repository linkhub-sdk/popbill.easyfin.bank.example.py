# -*- coding: utf-8 -*-
# code for console Encoding difference. Dont' mind on it
import imp
import sys

from popbill import ContactInfo, EasyFinBankService, PopbillException

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
연동회원 사업자번호에 담당자(팝빌 로그인 계정)를 추가합니다.
- https://developers.popbill.com/reference/easyfinbank/python/common-api/member#RegistContact
"""

try:
    print("=" * 15 + " 담당자 등록 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 담당자 정보
    newContact = ContactInfo(
        # 아이디
        id="TESTESTESTESTESTESTSETS",

        # 비밀번호
        Password="password123!@#",

        # 담당자 성명 (최대 100자)
        personName="담당자명",

        # 담당자 휴대폰 (최대 20자)
        tel="",

        # 담당자 메일 (최대 100자)
        email="",

        # 권한, 1(개인) 2(읽기) 3(회사)
        searchRole=3,
    )

    result = easyFinBankService.registContact(CorpNum, newContact)

    print("처리결과 : [%d] %s" % (result.code, result.message))
except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
