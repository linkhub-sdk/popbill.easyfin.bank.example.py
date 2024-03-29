# -*- coding: utf-8 -*-
# code for console Encoding difference. Dont' mind on it
import imp
import sys

from popbill import BankAccountInfo, EasyFinBankService, PopbillException

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
팝빌에 등록된 계좌정보를 수정합니다.
- https://developers.popbill.com/reference/easyfinbank/python/api/manage#UpdateBankAccount
"""

try:
    print("=" * 15 + " 계좌정보 수정 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    infoObj = BankAccountInfo(
        # 기관코드
        # 산업은행-0002 / 기업은행-0003 / 국민은행-0004 /수협은행-0007 / 농협은행-0011 / 우리은행-0020
        # SC은행-0023 / 대구은행-0031 / 부산은행-0032 / 광주은행-0034 / 제주은행-0035 / 전북은행-0037
        # 경남은행-0039 / 새마을금고-0045 / 신협은행-0048 / 우체국-0071 / KEB하나은행-0081 / 신한은행-0088 /씨티은행-0027
        BankCode="",
        # 계좌번호 하이픈('-') 제외
        AccountNumber="",
        # 계좌비밀번호
        AccountPWD="",
        # 계좌 별칭
        AccountName="",
        # 인터넷뱅킹 아이디 (국민은행 필수)
        BankID="",
        # 조회전용 계정 아이디 (대구은행, 신협, 신한은행 필수)
        FastID="",
        # 조회전용 계정 비밀번호 (대구은행, 신협, 신한은행 필수
        FastPWD="",
        # 메모
        Memo="",
    )

    result = easyFinBankService.updateBankAccount(CorpNum, infoObj)

    print("처리결과 : [%d] %s" % (result.code, result.message))
except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
