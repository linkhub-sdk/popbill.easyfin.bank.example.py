# -*- coding: utf-8 -*-
# code for console Encoding difference. Dont' mind on it
import sys
import imp

imp.reload(sys)
try:
    sys.setdefaultencoding("UTF8")
except Exception as E:
    pass

import testValue

from popbill import EasyFinBankService, PopbillException

easyFinBankService = EasyFinBankService(testValue.LinkID, testValue.SecretKey)
easyFinBankService.IsTest = testValue.IsTest
easyFinBankService.IPRestrictOnOff = testValue.IPRestrictOnOff
easyFinBankService.UseStaticIP = testValue.UseStaticIP
easyFinBankService.UseLocalTimeYN = testValue.UseLocalTimeYN

"""
연동회원 포인트 무통장 입금신청내역 1건을 확인합니다.
- https://developers.popbill.com/reference/easyfinbank/python/api/point#GetSettleResult
"""

try:
    print("=" * 15 + " 무통장 입금신청 정보 확인 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 정산코드 - 팝빌에서 임의 부여하는 값으로 PaymentRequest(연동회원 무통장 입금신청) 호출시 반환되는 값
    SettleCode = ""

    # 팝빌회원 팝빌 아이디
    UserID = testValue.testUserID

    paymentHistory = easyFinBankService.getPaymentHistory(CorpNum, SettleCode, UserID)

    print("결제 내용 ('포인트' / '정액제' / '미수금' 중 반환) : %s" % paymentHistory.productType)
    print("정액제 상품명 : %s" % paymentHistory.productName)
    print("결제유형 ('무통장' / '신용카드' / '실시간계좌이체' 중 반환) : %s" % paymentHistory.settleType)
    print("담당자명 : %s" % paymentHistory.settlerName)
    print("담당자메일 : %s" % paymentHistory.settlerEmail)
    print("결제금액 : %s" % paymentHistory.settleCost)
    print("충전포인트 : %s" % paymentHistory.settlePoint)
    print("결제상태 (1 / 2 / 3 / 4 / 5 중 반환) : %s" % paymentHistory.settleState)
    print("등록일시 (형식 : yyyyMMddHHmmss) : %s" % paymentHistory.regDT)
    print("상태일시 (형식 : yyyyMMddHHmmss) : %s" % paymentHistory.stateDT)


except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
