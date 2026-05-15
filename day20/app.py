# app.py: FastAPI 실행하는 파일
from fastapi import FastAPI
import uvicorn
app=FastAPI() # 1. FastAPI 객체 생성

# 2.
if __name__=='__main__':
    uvicorn.run('app:app', host='127.0.0.1', port=8000, reload=True)

# 3. 라우터: 여러 개 controller 파일들을 하나의 웹(서버) 연결
import controller
app.include_router(controller.router)