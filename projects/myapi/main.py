# 파이보 프로젝트를 설정하는 main.py 파일
# main.py 파일에 생성한 app 객체는 FastAPI의 핵심 객체이다. app 객체를 통해 FastAPI의 설정을 할 수 있다. main.py는 FastAPI 프로젝트의 전체적인 환경을 설정하는 파일이다.

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from domain.answer   import answer_router
from domain.question import question_router

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


app.include_router(question_router.router)
app.include_router(answer_router.router)