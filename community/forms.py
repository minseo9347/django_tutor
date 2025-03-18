# 형태 만들기
from django.forms import ModelForm
from community.models import Article
# 커뮤니티 폴더 밑에 모델스에서 폼이랑 아티클을 연결시키겠다.
class Form(ModelForm): # ModleForm을 상속받는다. -> 모델폼에 정의된 것을 가져와서 사용
    class Meta: # 함수 내부클래스로 정의
        model = Article # 아티클 모델을 사용하겠다는 의미
        fields = ['name', 'title', 'content', 'url', 'email']
        # 모델과 필드s 변수는 바꾸면 안됨, model.py에서 정의한 컬럼을 적는다.
        # 인용부호로 다 감싸주어야 한다.