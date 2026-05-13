
# FastAPI

# 1. import 가져오기
import uvicorn
from fastapi import FastAPI

# 2. fastAPI 객체 생성
app = FastAPI()

# 3. 서버 실행
if __name__ == "__main__":
    uvicorn.run( "T8-02:app" , host="127.0.0.1" , port=8000 , reload=True )

# 4. REST 정의하기
# REST: 자원 주고 받는 상태 구조
# REST API: HTTP로 REST 구현
# 자동으로 JSON 타입으로 응답한다. vs. @ResponseBody()
# 스프링부트의 @GetMapping("/URL") vs. @app.get("/URL")

@app.get("/")               # HTTP GET 방식으로 매핑. 주소 정의.
async def index():
    return "안녕 파이썬웹"

# 5. 쿼리 파라미터
@app.get("/user")
async def find_user(name, age: int):      # 기본타입 str -> 변경하려면 `변수명:타입명`으로 지정 가능 , URL?변수명=값&변수명=값
    return {'name':name , 'age':age , 'msg':'쿼리 파라미터 예시'}

# 6. 경로 파라미터
@app.get("/item/{name}/{age}")
async def find_item(name:str , age:int):
    return {'name':name, 'age':age, 'msg':'경로 파라미터 예시'}

# 7. 본문(body): POST/PUT
@app.post("/product")
async def find_product( product:dict ):     # `변수명:dict` -> 딕셔너리 타입으로 받기
    product['msg'] = 'body 본문 형식 예시'
    return product

# but, 8000웹에서는 바로 테스트 어려움
# RESTAPI 테스트: 1) TalendAPI , 2) Postman , 3) FastAPI DOCS
# 탈란드API: http://localhost:8000/product , {"name":"유재석","age":40} 
# FastAPI DOCS: http://localhost:8000/docs
