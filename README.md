# django_tutorial_42

# github 레포지토리
```
 - 레포지토리 이름 : django_tutorial_42  
 - README.md, .gitignore 파일 생성   
 - 로컬 컴퓨터와 연동하기           git clone git_url
```

# 프로젝트 생성
```
django-admin startproject django_tutor .

django_tutor = 파일이름
. = 현재 디렉토리에 프로젝트를 만든다.

```

# Django 기본 DB생성 명령
```
python manage.py migrate - 생성 명령
dir = db 생성 확인
```

# django 서버 실행 및 확인
```
python manage.py runserver
사용자 페이지 = http://127.0.0.1:8000/
관리자 페이지 = http://127.0.0.1:800/admin
```

# 관리자 아이디 만들기
```
python manamge.py createsuperuser

 Id : 
 Pw : 비밀번호 8자리 이상
```

# settings.py 기본설정 
```
 ALLOWED_HOSTS = ['localhost', '127.0.0.1’]
 LANGUAGE_CODE = 'ko-kr'
 TIME_ZONE = 'Asia/Seoul
```


# --------------------

# 장고 앱만들기
```
App 명 : community
python manage.py startapp community
```

# settings.py 설정
```
settings.py에서 installed_apps에 문자열로 'community',를 추가한다.
```

# 모델 만들기
```
models.py에 class를 활용해 모델을 만든다.
```

# DB적용
```
in 터미널 
python manage.py makemigrations = python -> db적용 파일 생성
python manage.py migrate = 생성된 파일을 실행하여 실제 DB에 테이블 반영
```

# url 패턴 만들기
```
url.py에서 경로를 설정한다.
URL을 community.views에서 가져온 write 뷰 함수에 연결한다.
```

# view 함수 정의
```
url을 통해 연결된 함수는 render 함수를 호출해 write.html 템플릿을 렌더링하고, 그 결과를 사용자에게 반환한다.
브라우저에서 http://127.0.0.1:8000/write/에 접속하면 write 뷰의 결과를 볼 수 있다.
```