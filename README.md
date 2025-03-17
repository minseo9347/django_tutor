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