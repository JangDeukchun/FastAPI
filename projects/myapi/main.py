from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

app = FastAPI() # FastAPI 클래스로 생성한 app객체가 바로 FastAPI의 핵심 객체이다. 모든 동작은 이 객체로부터 비롯된다.

# cors 헤더
origins = [
    "http://127.0.0.1:5173",    # 또는 "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/hello')
def hello():
    return {"message":"안녕하세요 파이보"}