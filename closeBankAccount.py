# -*- coding: utf-8 -*-
# code for console Encoding difference. Dont' mind on it
import sys
import imp
import testValue
from popbill import EasyFinBankService, PopbillException, BankAccountInfo

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
팝빌에 등록된 은행계좌의 정액제 해지를 요청한다.
'''

try:
    print("=" * 15 + " 계좌 정액제 해지신청 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 팝빌회원 아이디
    UserID = testValue.testUserID

    # [필수] 은행코드
    # 산업은행-0002 / 기업은행-0003 / 국민은행-0004 /수협은행-0007 / 농협은행-0011 / 우리은행-0020
    # SC은행-0023 / 대구은행-0031 / 부산은행-0032 / 광주은행-0034 / 제주은행-0035 / 전북은행-0037
    # 경남은행-0039 / 새마을금고-0045 / 신협은행-0048 / 우체국-0071 / KEB하나은행-0081 / 신한은행-0088 /씨티은행-0027
    BankCode = ""

    # [필수] 계좌번호 하이픈('-') 제외
    AccountNumber = ""

    # 해지유형, "일반", "중도" 중 선택기재
    # 일반해지 - 이용중인 정액제 사용기간까지 이용후 정지
    # 중도해지 - 요청일 기준으로 정지, 정액제 잔여기간은 일할로 계산되어 포인트 환불
    CloseType = "중도"

    result = easyFinBankService.closeBankAccount(CorpNum, BankCode, AccountNumber, CloseType, UserID)

    print("처리결과 : [%d] %s" % (result.code, result.message))
except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
