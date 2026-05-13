
# 1. 통계 데이터 조회 API . GET /stats
#   2. 반환 데이터
#     가. 평균 가격
#     나. 최고 가격
#     다. 최저 가격
#     라. 가장 많이 출판된 연도
#   3. 응답 예시
# {   "평균가격": 17200,
#     "최고가격": 45000,
#     "최저가격": 5900,
#     "최다출판연도": 2024  }

from fastapi import APIRouter
router=APIRouter(prefix="/stats")
from service import book_service

@router.get("/result")
async def result():
    return book_service.result( )
