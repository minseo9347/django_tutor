# ctrl + . 으로 쉽게 import 할 수 있다.
from django.shortcuts import render
from community.models import Article


def index(request):
    # article 테이블에서 최근글 3개를 쿼리(조회)한다. #order_by는 정렬
    latest_article_list = Article.objects.all().order_by('-cdate')[:3]
    print(latest_article_list)
    return render(request, 'index.html', {'latest_article_list': latest_article_list})