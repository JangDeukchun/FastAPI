from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import SessionLocal, get_db
from models import Question


router = APIRouter( # 라우터 파일에 반드시 필요한 것은 APIRouter 클래스로 생성한 router 객체이다. router 객체를 생성하여 FastAPI 앱에 등록해야만 라우팅 기능이 동작한다.
    prefix="/api/question", # 여기부터 시작인거지 
)

# 오류 여부에 상관없이 with문을 벗어나는 순간 db.close()가 실행되므로 보다 안전한 코드로 변경된 것이다.
@router.get("/list")
def question_list():
    with get_db() as db:
        _question_list = db.query(Question).order_by(Question.create_date.desc()).all()
    return _question_list


# # FastAPI의 Depends를 사용하면 with문을 사용하는 것 보다 더 간단하게 사용할수 있다.
# @router.get("/list")
# def question_list(db: Session = Depends(get_db)):
#     _question_list = db.query(Question).order_by(Question.create_date.desc()).all()
#     return _question_list