
# (app.py로 router 가져감)

# [ 1. 라우터: 특정 도메인(주소)을 한 곳에 묶어주는 역할 ]
from fastapi import APIRouter

# `APIRouter( prefix='/공통도메인' )` vs. `@ReqeustMapping("/공통도메인")`
router = APIRouter( prefix= "/api" )   
    # 이걸 app.py의 app=FastAPI()에다가 (라우터)연결 해줘야 한다.

# [ 3. 서비스(service) 불러오기 ]
from service import item_service    # service.py에서 서비스 객체를 가져온다.

# [ 2. REST API 정의 ]
# 1. GET
@router.get("/item")
async def item(id: int):
    return item_service.item( id )  # `서비스객체.함수(변수값)`

# 2. GET
@router.get("/items")
async def items():
    return item_service.items()

# 3. POST: `{'id':3, 'name':'제로콜라', 'price':2000}`
@router.post("/save")
async def save(item:dict):
    return item_service.save( item )

# 4. PUT
@router.put("/update")
async def update(item:dict):
    return item_service.update( item )

# 5. DELETE
@router.delete("/item")
async def delete(id: int):
    return item_service.delete( id )
