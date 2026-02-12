"""
라우트 (Controller Layer)
- 사용자가 요청한 URL을 처리하고
- 서비스 계층을 호출해서 DB 조작
- 결과를 템플릿에 전달
"""

# 웹에서 요청을 받고 검증? 해서 요청에 따른 적합한 서비스를 결정하는 곳

# TODO: get_all_reviews, create_review, get_review_by_id,
#       update_review, delete_review 함수를 불러오세요

from flask import Blueprint, render_template, request, redirect, url_for
from app.services.review_service import (
    get_all_reviews,
    create_review,
    get_review_by_id,
    update_review,
    delete_review,
)

# 블루프린트 생성
review_bp = Blueprint("review", __name__)

@review_bp.route("/")
def index():
    """리뷰 목록 + 평균 별점"""
    # TODO: 리뷰 목록을 가져오세요 (service의 get_all_reviews)
    reviews = get_all_reviews()

    # TODO: 평균 별점을 계산하세요 (리뷰가 있으면 rating 평균, 없으면 0)
    if reviews:
        avg_rating = sum(r.rating for r in reviews) / len(reviews)
        avg_rating = round(avg_rating, 2) #avg_rating 2으로 숫자 가독성 향상
    else:
        avg_rating = 0

    # TODO: index.html 템플릿에 reviews, avg_rating을 전달해서 렌더링하세요
    return render_template("index.html", reviews=reviews, avg_rating=avg_rating)


@review_bp.route("/new", methods=["GET", "POST"])
def new_review():
    """새 리뷰 작성"""
    # TODO: request.method 가 POST 인지 확인하세요
    # TODO: form 데이터(title, content, rating)를 받아오세요
    if request.method == "POST":
        title = request.form.get("title", "").strip()
        content = request.form.get("content", "").strip()
        rating_raw = request.form.get("rating", "").strip()

        if not title or not content or not rating_raw:
            return render_template("new.html", error="모든 항목을 입력하세요.")

        try:
            rating = int(rating_raw)
        except ValueError:
            return render_template("new.html", error="별점은 숫자여야 합니다.")

        # TODO: service의 create_review 함수를 호출해서 DB에 저장하세요
        create_review(title=title, content=content, rating=rating)
        
        # TODO: 저장 후 index 페이지로 redirect 하세요
        return redirect(url_for("review.index"))
    
        # TODO: GET 요청일 경우 new.html 템플릿을 렌더링하세요
    return render_template("new.html")


@review_bp.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_review(id):
    """리뷰 수정"""
    # TODO: service의 get_review_by_id 함수로 해당 id의 리뷰를 가져오세요
    review = get_review_by_id(id)

    if review is None:
        return redirect(url_for("review.index"))
    # TODO: POST 요청일 경우 수정된 데이터(title, content, rating)를 받아서 service의 update_review 실행

    if request.method == "POST":
        title = request.form.get("title", "").strip()
        content = request.form.get("content", "").strip()
        rating_raw = request.form.get("rating", "").strip()

        if not title or not content or not rating_raw:
            return render_template("edit.html", review=review, error="모든 항목을 입력하세요.")

        try:
            rating = int(rating_raw)
        except ValueError:
            return render_template("edit.html", review=review, error="별점은 숫자로만 입력해야 합니다.")

    # TODO: 수정 후 index 페이지로 redirect 하세요
        update_review(review_id=id, title=title, content=content, rating=rating)
        return redirect(url_for("review.index"))

    # TODO: GET 요청일 경우 edit.html 템플릿을 렌더링하세요 (review 전달)
    return render_template("edit.html", review=review)


@review_bp.route("/delete/<int:id>")
def delete_review_route(id):
    """리뷰 삭제"""
    # TODO: service의 delete_review 함수를 실행해서 해당 리뷰를 삭제하세요
    delete_review(review_id=id)
    # TODO: 삭제 후 index 페이지로 redirect 하세요
    return redirect(url_for("review.index"))