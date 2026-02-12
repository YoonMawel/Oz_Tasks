# 실행 스크립트 역할
# 실행 시 동시에 config.py도 실행된다고 보면 됨
from app import create_app

# run.py가 create_app()을 호출해서 Flask 앱 객체를 생성
app = create_app()

# Flask 개발 서버 실행
# DEBUG True면 코드 수정 시 자동 재시작 + 에러 표시
if __name__ == "__main__":
    app.run(debug=True)