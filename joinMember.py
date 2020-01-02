# -*- coding: utf-8 -*-
# code for console Encoding difference. Dont' mind on it
import sys
import imp
import testValue

from popbill import JoinForm, EasyFinBankService, PopbillException

imp.reload(sys)
try:
    sys.setdefaultencoding('UTF8')
except Exception as E:
    pass

easyFinBankService = EasyFinBankService(testValue.LinkID, testValue.SecretKey)
easyFinBankService.IsTest = testValue.IsTest
easyFinBankService.IPRestrictOnOff = testValue.IPRestrictOnOff

'''
팝빌 연동회원 가입을 요청합니다.
'''

try:
    print("=" * 15 + " 연동회원 가입 " + "=" * 15)

    # 회원정보
    newMember = JoinForm(

        # 아이디 (6자 이상 50자 미만)
        ID="join_id_test",

        # 비밀번호 (6자 이상 20자 미만)
        PWD="this_is_password",

        # 사업자번호 "-" 제외
        CorpNum="0000000000",

        # 대표자성명 (최대 100자)
        CEOName="테스트대표자성명",

        # 상호 (최대 200자)
        CorpName="테스트가입상호",

        # 주소 (최대 300자)
        Addr="테스트회사주소",

        # 업태 (최대 100자)
        BizType="테스트업태",

        # 종목 (최대 100자)
        BizClass="테스트업종",

        # 담당자 성명 (최대 100자)
        ContactName="담당자성명",

        # 담당자 이메일주소 (최대 100자)
        ContactEmail="test@test.com",

        # 담당자 연락처 (최대 20자)
        ContactTEL="070-111-222",

        # 담당자 휴대폰번호 (최대 20자)
        ContactHP="010-111-222",
    )

    result = easyFinBankService.joinMember(newMember)

    print("처리결과 : [%d] %s" % (result.code, result.message))
except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
