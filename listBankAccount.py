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
easyFinBankService.UseLocalTimeYN = testValue.UseLocalTimeYN

'''
팝빌에 등록된 계좌 목록을 확인합니다.
- https://docs.popbill.com/easyfinbank/python/api#ListBankAccount
'''

try:
    print("=" * 15 + " 계좌 목록 확인 " + "=" * 15 + "\n")

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    response = easyFinBankService.listBankAccount(CorpNum)

    for info in response:
        print("accountNumber (계좌번호) : %s" % info.accountNumber)
        print("bankCode (기관코드) : %s" % info.bankCode)
        print("accountName (계좌별칭) : %s" % info.accountName)
        print("accountType (계좌유형) : %s" % info.accountType)
        print("state (계좌 정액제 상태) : %s" % info.state)
        print("regDT (등록일시) : %s" % info.regDT)
        print("memo (메모) : %s" % info.memo)
        print("contractDT (정액제 서비스 시작일시) : %s" % info.contractDT)
        print("useEndDate (정액제 서비스 종료일) : %s" % info.useEndDate)
        print("baseDate (자동연장 결제일) : %s" % info.baseDate)
        print("contractState (정액제 서비스 상태) : %s" % info.contractState)
        print("closeRequestYN (정액제 서비스 해지신청 여부) : %s" % info.closeRequestYN)
        print("useRestrictYN (정액제 서비스 사용제한 여부) : %s" % info.useRestrictYN)
        print("closeOnExpired (정액제 서비스 만료 시 해지 여부) : %s" % info.closeOnExpired)
        print("unPaidYN (미수금 보유 여부) : %s" % info.unPaidYN+ '\n')

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
