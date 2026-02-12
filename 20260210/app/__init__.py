from flask import Flask
from selenium.webdriver.common.devtools.v142.tethering import bind
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, scoped_session
from .config import Config

# DB 연결 엔진을 생성 (create_engine)
engine = create_engine(
    Config.SQLALCHEMY_DATABASE_URI,
    echo=getattr(Config, "SQLALCHEMY_ECHO", False),
    future=True,
)

# 세션(SessionLocal) 객체(scoped_session)
SessionLocal = scoped_session( # 요청 단위로 안전하게 관리
    sessionmaker(
        bind=engine,
        autoflush=False,
        autocommit=False,
        expire_on_commit=False,
    )
)

# Base 클래스 생성 !!!
Base = declarative_base()

def create_app():
    # 1. Flask 앱 생성
    app = Flask(__name__)
    app.config.from_object(Config)

    # 2. 모델을 import
    from . import models

    # DB에 테이블이 없으면 생성하게끔 Base 실행
    Base.metadata.create_all(bind=engine)

    # 블루프린트(review_bp)를 등록하여 URL 규칙을 Flask에 연결
    from .routes import review_routes
    app.register_blueprint(review_routes.review_bp)

    # 요청이 끝날 때마다 세션 닫기
    @app.teardown_appcontext
    def shutdown_session(exception=None):
        SessionLocal.remove()

    return app