import contextlib

# database.py 파일은 데이터베이스와 관련된 설정을 하는 파일이다. 이 파일에는 데이터베이스를 사용하기 위한 변수, 함수등을 정의하고 접속할 데이터베이스의 주소와 사용자, 비밀번호등을 관리한다.
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base # 데이터베이스 모델을 구성할 때 사용되는 클래스
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./myapi.db" # db 접속 주소, sqlite:///./myapi.db는 데이터베이스의 파일을 의미하며 프로젝트 루트 디렉토리에 저장한다는 의미이다.

# 컨넥션 풀은 데이터 베이스에 접속하는 세션수를 제어하고, 또 세션 접속에 소요되는 시간을 줄이고자 하는 용도로 사용한다
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args = {'check_same_thread':False}
)

# 데이터 베이스에 접속하기 위한 클래스
# autocommit=False로 설정하면 데이터를 변경했을때 commit 이라는 사인을 주어야만 실제 저장이 된다. 만약 autocommit=True로 설정할 경우에는 commit이라는 사인이 없어도 즉시 데이터베이스에 변경사항이 적용된다.
# utocommit=False인 경우에는 데이터를 잘못 저장했을 경우 rollback 사인으로 되돌리는 것이 가능하지만 autocommit=True인 경우에는 commit이 필요없는 것처럼 rollback도 동작하지 않는다는 점에 주의해야 한다.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)



Base = declarative_base() # 데이터베이스 모델을 구성할 때 사용되는 클래스


# 프로그래밍에서 "Dependency Injection(의존성 주입)"의 뜻은 필요한 기능을 선언하여 사용할 수 있다는 의미이다.
@contextlib.contextmanager
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()