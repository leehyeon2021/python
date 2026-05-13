
# 파이썬 웹 프레임워크 

# FastAPI: 파이썬 웹 프레임워크
# 특징: RESTAPI, API 문서 자동 등등
# 사용처: 데이터분석, AI모델(머신러닝/딥러닝) 서버       , 탈란드API 대신 사용 가능
# * 장고(Django)보다 가벼움

# https://fastapi.tiangolo.com/ko/
# 1. 설치: `pip install "fastapi[standard]"`
# 2. import: `import uvicorn`, `from fastapi import FastAPI`
# 3. app 객체 생성: 자바와 다르게 파이썬은 인스턴스 생성시 new 없음.
# 4. uvicorn.run("파일명:app")으로 서버 실행
# 5. 서버 접속: http://localhost:8000/ , http://127.0.0.1:8000 , http://localhost:8000/docs -> FastAPI가 자동으로 만들어줌
# 6. 서버 종료: 터미널 종료 또는 ctrl+c

import uvicorn                  # 파이썬 서버(주로 8000). 자바의 톰캣(WAS) 역할
from fastapi import FastAPI     # REST 정의 역할. 자바의 SPRINGWEB 역할

# app 객체 생성 (파이썬은 new 없음)
app = FastAPI()

# 모듈(.py) 실행 시작점
if __name__ == "__main__" :     # 자바의 main 함수 역할 (만약 현재 이름이 main이면)
    # uvicorn.run( "파일명:app" , host="127.0.0.1" , port=8000 , reload=True )  -> 자바의 spring run
    uvicorn.run( "T8-01:app" , host="127.0.0.1" , port=8000 , reload=True ) # reload는 실시간 코드수정사항 반영기능 