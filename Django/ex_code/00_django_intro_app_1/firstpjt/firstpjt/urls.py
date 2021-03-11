"""firstpjt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from articles import views


urlpatterns = [
    # 'admin/' 얘는 주소를 의미. 서버를 켜서 주소 뒤에 /admin이라고 넣어주면 해당 페이지로 이동
    path('admin/', admin.site.urls),
    # url을 만들어가는 과정
    
    # 메인페이지 만들기. 메인의 주소는 일반적으로 index라고 지정
    # path의 두번째 인자는 만약 url주소가 index로 요청이 들어왔을 때, 어떤 view 함수를 실행시킬건지? 
    # 따라서 메인 페이지를 보여주는 view 함수르 호출을 할거고 -> 그 함수가 view에 있어야하니까 view로 이동해서 함수 만들어주기.
    # 만들어진 함수 이름을 두번째 인자로 넣기(다른 위치에 있으니까 경로도 알려주기 - from articles import views)
    # views.index : views 안에 있는 인덱스라는 함수가져오기
    path('index/', views.index),
    # 즉 사용자의 요청이 index라는 주소값으로 들어온다면 urls.py가 그 url을 인식해서 views.index이걸 호출할거야 라는 의미

    # greeting 이라는 주소가 넘어오면 views에 있는 greeting 함수 실행.
    path('greeting/', views.greeting),

    # 필터 쓰기
    path('dinner/', views.dinner),


    path('throw/', views.throw),
    path('catch/', views.catch),
    
]
