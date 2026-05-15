
# 3. 라우터 : 앱(서버) 와 연결 되는 라우터
from fastapi import APIRouter
router = APIRouter( prefix="/api")

# 4. 서비스객체 호출
from service import productService 

# 5. HTTP 매핑
@router.get("/products")
async def products( ) :
    return productService.products( )
# 스프링과의 통신은 아래 거랑 해야 함
# http://127.0.0.1:8000/api/spring
# 통신 구조: 브라우저 -> 파이썬 -> 스프링
@router.get("/spring")
async def getSpring( ) :
    return await productService.getSpring()