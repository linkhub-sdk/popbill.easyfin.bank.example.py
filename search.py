# -*- coding: utf-8 -*-
# code for console Encoding difference. Dont' mind on it
import imp
import sys

import testValue
from popbill import EasyFinBankService, PopbillException

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
수집 상태 확인(GetJobState API) 함수를 통해 상태 정보가 확인된 작업아이디를 활용하여 계좌 거래 내역을 조회합니다.
- https://developers.popbill.com/reference/easyfinbank/python/api/search#Search
"""

try:
    print("=" * 15 + " 수집 결과 조회 " + "=" * 15)

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

    # 페이지번호
    Page = 1

    # 페이지당 목록개수, 최대값 1000
    PerPage = 10

    # 정렬방향 D-내림차순, A-오름차순
    Order = "D"

    response = easyFinBankService.search(
        CorpNum, JobID, TradeType, SearchString, Page, PerPage, Order
    )

    print("code (응답코드) : %s " % response.code)
    print("message (응답메시지) : %s " % response.message)
    print("total (검색결과 건수) : %s " % response.total)
    print("perPage (페이지당 검색개수) : %s " % response.perPage)
    print("pageNum (페에지 번호) : %s " % response.pageNum)
    print("pageCount (페이지 개수) : %s " % response.pageCount)
    print("lastScrapDT (최종 조회일시) : %s \n" % response.lastScrapDT)
    print("balance (현재 잔액) : %s \n" % response.lastScrapDT)

    for info in response.list:
        print("\n==============거래내역 정보==============")
        print("tid (거래내역 아이디) : %s" % info.tid)
        print("trdate (거래일자) : %s" % info.trdate)
        print("trserial (거래일자별 거래내역 순번) : %s" % info.trserial)
        print("trdt (거래일시) : %s" % info.trdt)
        print("accIn (입금액) : %s" % info.accIn)
        print("accOut (출금액) : %s" % info.accOut)
        print("balance (잔액) : %s" % info.balance)
        print("remark1 (비고1) : %s" % info.remark1)
        print("remark2 (비고2) : %s" % info.remark2)
        print("remark3 (비고3) : %s" % info.remark3)
        print("memo (메모) : %s \n" % info.memo)

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
