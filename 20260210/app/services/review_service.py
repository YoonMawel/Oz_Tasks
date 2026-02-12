"""
서비스 계층 (Service Layer)
- 라우트에서 직접 DB 조작하지 않고
- 이 모듈을 거쳐서 DB CRUD 실행
"""
# 실질적인 db 로직 실행 모듈은 routes가 아니라 service가 맞음

from app import SessionLocal
from app.models import Review


def get_all_reviews():
    """모든 리뷰 조회"""
    # TODO: DB 세션을 열고 모든 리뷰를 조회하세요
    db = SessionLocal()
    
    try:
        return db.query(Review).order_by(Review.id.desc()).all()
    finally:
        
        db.close()


def create_review(title, content, rating):
    """리뷰 생성"""
    # TODO: Review 객체를 생성하고 DB에 추가한 뒤 commit 하세요
    db = SessionLocal()
    try:
        review = Review(title=title, content=content, rating=rating)
        db.add(review)
        db.commit()
        db.refresh(review)
        return review
    
    except Exception:
        db.rollback()
        raise
    
    finally:
        db.close()


def get_review_by_id(review_id):
    """ID로 리뷰 조회"""
    # TODO: review_id 에 해당하는 리뷰를 DB에서 조회하세요
    db = SessionLocal()
    try:
        return db.query(Review).filter(Review.id == review_id).first()
    finally:
        db.close()


def update_review(review_id, title, content, rating):
    """리뷰 수정"""
    # TODO: review_id 에 해당하는 리뷰를 조회 후, 필드를 수정하고 commit 하세요
    db = SessionLocal()
    try:
        review = db.query(Review).filter(Review.id == review_id).first()
        if review is None:
            return None

        review.title = title
        review.content = content
        review.rating = rating

        db.commit()
        db.refresh(review)
        return review
    
    except Exception:
        db.rollback()
        raise
    
    finally:
        db.close()


def delete_review(review_id):
    """리뷰 삭제"""
    # TODO: review_id 에 해당하는 리뷰를 DB에서 삭제하고 commit 하세요
    db = SessionLocal()
    try:
        review = db.query(Review).filter(Review.id == review_id).first()
        
        if review is None:
            return False

        db.delete(review)
        db.commit()
        
        return True
    except Exception:
        db.rollback()
        raise
    
    finally:
        db.close()