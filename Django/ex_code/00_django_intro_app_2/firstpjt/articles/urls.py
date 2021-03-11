from django.urls import path
from . import views

urlpatterns = [
    # 메인페이지 만들기. 메인의 주소는 일반적으로 index라고 지정
    # path의 두번째 인자는 만약 url주소가 index로 요청이 들어왔을 때, 어떤 view 함수를 실행시킬건지? 
    # 따라서 메인 페이지를 보여주는 view 함수르 호출을 할거고 -> 그 함수가 view에 있어야하니까 view로 이동해서 함수 만들어주기.
    # 만들어진 함수 이름을 두번째 인자로 넣기(다른 위치에 있으니까 경로도 알려주기 - from articles import views)
    # views.index : views 안에 있는 인덱스라는 함수가져오기
    path('index/', views.index, name='index'),
    # 즉 사용자의 요청이 index라는 주소값으로 들어온다면 urls.py가 그 url을 인식해서 views.index이걸 호출할거야 라는 의미

    # greeting 이라는 주소가 넘어오면 views에 있는 greeting 함수 실행.
    path('greeting/', views.greeting, name='greeting'),

    # 필터 쓰기
    path('dinner/', views.dinner, name='dinner'),


    path('throw/', views.throw, name='throw'),
    path('catch/', views.catch, name='catch'),

    path('hello/<str:name>/', views.hello, name='hello'),


    
]