from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from database import Base

class Question(Base):
    __tablename__ = "question"

    id = Column(Integer, primary_key=True)
    subject = Column(String, nullable=False) # 글자 수 제한 가능
    content = Column(Text, nullable=False) # 글자 수 제한 x
    create_date = Column(DateTime, nullable=False)

class Answer(Base):
    __tablename__ = "answer"

    id = Column(Integer, primary_key=True)
    content = Column(Text, nullable=False)
    create_date = Column(DateTime, nullable=False)
    question_id = Column(Integer, ForeignKey("question.id")) # 데이터베이스에서는 기존 모델과 연결된 속성을 외부 키(foreign key)라고 한다.
    question = relationship("Question", backref="answers") # backref는 역참조 설정이다. 질문에서 답변을 거꾸로 참조하는 것을 의미
    
    
    
    