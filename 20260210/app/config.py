# Flask 설정 파일

import os

# instance 폴더 경로
INSTANCE_DIR = os.path.join(os.path.dirname(__file__), "..", "instance")

# 폴더가 없으면 생성
os.makedirs(INSTANCE_DIR, exist_ok=True)

class Config:
    """환경 설정 (로컬 SQLite 기본값)"""
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///instance/reviews.db")