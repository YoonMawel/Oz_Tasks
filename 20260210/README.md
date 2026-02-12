# Flask로 CRUD 전체 구현

#### 1. CRUD

> 로직은 **review_service.py**에 구현
>
> URL 노출 → 사용자 입력을 받는 곳은 **review_routes.py**에 구현
> 
> CRUD의 대상이 되는 데이터 구조(테이블)을 정의하는 곳은 **models.py**
> 
> CRUD의 결과를 화면에 출력(보여주는) 모듈은 <br> > **index.html**, **new.html**, **edit.html**

※ 즉, CRUD의 실제 DB 조작은 **review_service.py** <br>
URL ↔ 화면 흐름의 담당은 **review_routes.py** <br>
CRUD 대상 스키마 정의는 **models.py** <br>
화면 렌더링은 **/template**

<br>

## 프로젝트가 돌아가는 과정

**요약**: Request → Route → Service → DB(models/Session) → Template → 브라우저로부터 응답

>**1.** 즉, 라우트(Route)가 **요청 및 검증**을 받고 어떤 서비스를 호출할 지 결정 <br>
>**2.** 라우트에서 결정한 서비스에 따라 DB 로직을 실행 (CRUD, commit, rollback 등)<br>
>**3.** 호출과 로직 처리의 결과를 템플릿(template)을 통해 HTML을 렌더링, 그리고 **화면에 출력**

<br>
