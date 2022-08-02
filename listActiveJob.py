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
수집 요청(RequestJob API) 함수를 통해 반환 받은 작업아이디의 목록을 확인합니다.
- 수집 요청 후 1시간이 경과한 수집 요청건은 상태정보가 반환되지 않습니다.
- https://docs.popbill.com/easyfinbank/python/api#ListActiveJob
'''

try:
    print("=" * 15 + " 수집 상태 목록 확인 " + "=" * 15 + "\n")

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    response = easyFinBankService.listActiveJob(CorpNum)

    for info in response:
        print("jobID (작업아이디) : %s" % info.jobID)
        print("jobState (수집상태) : %s" % info.jobState)
        print("startDate (시작일자) : %s" % info.startDate)
        print("endDate (종료일자) : %s" % info.endDate)
        print("errorCode (오류코드) : %s" % info.errorCode)
        print("errorReason (오류메시지) : %s" % info.errorReason)
        print("jobStartDT (작업 시작일시) : %s" % info.jobStartDT)
        print("jobEndDT (작업 종료일시) : %s" % info.jobEndDT)
        print("regDT (수집 요청일시) : %s" % info.regDT + '\n')


except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
