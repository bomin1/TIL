from django.shortcuts import render
import random

# Create your views here.

# view 함수의 첫번째 인자는 반드시 request
def index(request):

    # 네이버를 들어가건 어디를 들어가건 우리가 보는 것은 결국 html문서 하나
    # 이 함수가 데이터들을 조합해서 하나의 완성된 템플릿을 만들어야 하는데
    # 조합할 데이터가 없으니까 하나의 문서를 보여주고 싶다
    # render : 잘 포장해서 보여주겠다
    # 두번째 인자로 템플릿의 경로 작성.
    # 템플릿 만들러 가야함(html)
    # 만들고 와서 장고는 templates라는 경로는 이미 알고있어서 이 이후의 값들만 두번째 인자로 넣어주면 됨.
    return render(request, 'index.html')
    # 랜더도 request 첫번째 인자로 무조건!

def greeting(request):
    # greeting.html을 보여줄거다.

    # 템플릿에서 변수가 출력되기 위해서는 템플릿에 변수가 전달되어야함. 
    # 세번째 인자로 전달
    # 즉 greeting.html에 context에 들어있는거 전달.(딕셔너리)
    
    foods = ['a','b','c','d','e',]
    info = {
        'name':'Harry'
    }
    context = {
        'info' : info,
        'foods' : foods,
    }
    return render(request, 'greeting.html', context)

def dinner(request):
    foods=['족발','피자','햄버거','치킨']
    pick=random.choice(foods)
    context = {
        'pick':pick,
        'foods': foods,
    }
    return render(request, 'dinner.html', context)

def throw(request):
    return render(request, 'throw.html')

def catch(request):
    message = request.GET.get('message')
    context = {
        'message':message,
    }
    return render(request, 'catch.html', context)