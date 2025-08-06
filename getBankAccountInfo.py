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
팝빌에 등록된 계좌정보를 확인합니다.
- https://developers.popbill.com/reference/easyfinbank/python/api/manage#GetBankAccountInfo
"""

try:
    print("=" * 15 + " 계좌정보 확인 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 기관코드
    BankCode = ""

    # 계좌번호
    AccountNumber = ""

    info = easyFinBankService.getBankAccountInfo(CorpNum, BankCode, AccountNumber)

    print("accountNumber (계좌번호) : %s" % info.accountNumber)
    print("bankCode (기관코드) : %s" % info.bankCode)
    print("accountName (계좌별칭) : %s" % info.accountName)
    print("accountType (계좌유형) : %s" % info.accountType)
    print("state (계좌 상태) : %s" % info.state)
    print("regDT (계좌 등록일시) : %s" % info.regDT)
    print("contractDT (정액제 서비스 시작일시) : %s" % info.contractDT)
    print("useEndDate (정액제 서비스 종료일) : %s" % info.useEndDate)
    print("baseDate (자동연장 결제일) : %s" % info.baseDate)
    print("contractState (정액제 서비스 상태) : %s" % info.contractState)
    print("closeRequestYN (정액제 서비스 해지신청 여부) : %s" % info.closeRequestYN)
    print("useRestrictYN (정액제 서비스 사용제한 여부) : %s" % info.useRestrictYN)
    print("closeOnExpired (정액제 서비스 만료 시 해지 여부) : %s" % info.closeOnExpired)
    print("unPaidYN (미수금 보유 여부) : %s" % info.unPaidYN)
    print("memo (메모) : %s" % info.memo + "\n")

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
