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
수집 상태 확인(GetJobState API) 함수를 통해 상태 정보가 확인된 작업아이디를 활용하여 계좌 거래내역의 요약 정보를 조회합니다.
- 요약 정보 : 입·출 금액 합계, 입·출 거래 건수
- https://developers.popbill.com/reference/easyfinbank/python/api/search#Summary
'''

try:
    print("=" * 15 + "수집 결과 요약정보 조회 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 수집요청(requestJob)시 발급받은 작업아이디
    JobID = "022080215000000325"

    # 거래유형 배열 ("I" 와 "O" 중 선택, 다중 선택 가능)
    # └ I = 입금 , O = 출금
    # - 미입력 시 전체조회
    TradeType = ["I", "O"]

    # "입·출금액" / "메모" / "비고" 중 검색하고자 하는 값 입력
    # - 메모 = 거래내역 메모저장(SaveMemo)을 사용하여 저장한 값
    # - 비고 = EasyFinBankSearchDetail의 remark1, remark2, remark3 값
    # - 미입력시 전체조회
    SearchString = ""

    response = easyFinBankService.summary(CorpNum, JobID, TradeType, SearchString)


    print("count (수집 결과 건수) : %s " % response.count)
    print("cntAccIn (입금거래 건수) : %s " % response.cntAccIn)
    print("cntAccOut (출금거래 건수) : %s " % response.cntAccOut)
    print("totalAccIn (입금액 합계) : %s " % response.totalAccIn)
    print("totalAccOut (출금액 합계) : %s " % response.totalAccOut)

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
