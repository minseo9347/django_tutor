from django.shortcuts import render
# 사용자의 입력 가능란을 만든다.
from community.forms import Form
# 커뮤니티 밑에 폼즈에서 폼을 가져온다.
# Create your views here.
def write(request): # request는 네트워크 통신으로 전달받은 것, 즉 인터넷에 https를 적은 그 자체
    # 비즈니스 로직 구현 ex) db와 통신
    
    form = Form() # 메모리로 저장하기 위해 폼을 가져오고 객체변수에 담는다.

    hello = "안녕" # -> html에 넘겨주어야 한다.
    # 사용자 method가 post일 경우
    if request.method == 'POST':
        # request 데이터를 폼객체로 생성
        form = Form(request.POST)
        # print(form)
        if form.is_valid(): # 데이터 유효성 검증
            # DB데이블에 저장
            form.save()

    else:
        form = Form
    # return render(request, 'write.html', {'키':파이썬변수}) # request,
    # return render(request, 'write.html',{'hello_django:':hello})
    # hello를 html에 넣어라 # html은 브라우저에서 해석되기 때문에 파이썬을 직접해석할 수 없고 연결시키기 위해 딕셔너리로 넣어야 한다.
    # 그러므로 파이썬 내용을 키값에 대입하여 html 문서에 작성한다. -> community에 templates 문서이름인 write.html에 키값을 넣는다.
    return render(request, 'write.html', {'hello_django':hello,'form':form})