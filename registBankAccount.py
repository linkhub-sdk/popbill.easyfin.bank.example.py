# -*- coding: utf-8 -*-
# code for console Encoding difference. Dont' mind on it
import sys
import imp
import testValue

from popbill import BankAccountInfo, EasyFinBankService, PopbillException

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
팝빌에 계좌정보를 등록합니다.
- https://developers.popbill.com/reference/easyfinbank/python/api/manage#RegistBankAccount
"""

try:
    print("=" * 15 + " 계좌 등록 " + "=" * 15)

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
        # 계좌유형, "법인" 또는 "개인" 입력
        AccountType="",
        # 예금주 식별정보 ('-' 제외)
        # 계좌유형이 "법인"인 경우 : 사업자번호(10자리)
        # 계좌유형이 "개인"인 경우 : 예금주 생년월일 (6자리-YYMMDD)
        IdentityNumber="",
        # 계좌 별칭
        AccountName="",
        # 인터넷뱅킹 아이디 (국민은행 필수)
        BankID="",
        # 조회전용 계정 아이디 (대구은행, 신협, 신한은행 필수)
        FastID="",
        # 조회전용 계정 비밀번호 (대구은행, 신협, 신한은행 필수
        FastPWD="",
        # 결제기간(개월), 1~12 입력가능, 미기재시 기본값(1) 처리
        # - 파트너 과금방식의 경우 입력값에 관계없이 1개월 처리
        UsePeriod="1",
        # 메모
        Memo="",
    )

    result = easyFinBankService.registBankAccount(CorpNum, infoObj)

    print("처리결과 : [%d] %s" % (result.code, result.message))
except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
