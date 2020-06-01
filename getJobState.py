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
계좌 거래내역 수집 상태를 확인합니다.
- https://docs.popbill.com/easyfinbank/python/api#GetJobState
'''

try:
    print("=" * 15 + " 수집 상태 확인 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 팝빌회원 아이디
    UserID = testValue.testUserID

    # 수집요청(requestJob) 호출시 발급받은 작업아이디
    jobID = "020010214000000009"

    response = easyFinBankService.getJobState(CorpNum, jobID, UserID)

    print("jobID (작업아이디) : %s" % response.jobID)
    print("jobState (수집상태) : %s" % response.jobState)
    print("startDate (시작일자) : %s" % response.startDate)
    print("endDate (종료일자) : %s" % response.endDate)
    print("errorCode (오류코드) : %s" % response.errorCode)
    print("errorReason (오류메시지) : %s" % response.errorReason)
    print("jobStartDT (작업 시작일시) : %s" % response.jobStartDT)
    print("jobEndDT (작업 종료일시) : %s" % response.jobEndDT)
    print("regDT (수집 요청일시) : %s" % response.regDT)

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
