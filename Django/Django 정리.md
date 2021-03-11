## 1. 프로젝트 만들기

```bash
$ django-admin startproejct 플젝이름 : 프로젝트 생성 명렁어
```

```bash
$ python manage.py runserver 서버구동
```



## 2. 어플리케이션 만들기

> **일반적으로 app 이름은 `복수형`으로 작성 하는 것을 권장**

```bash
$ python manage.py startapp 어플리케이션이름(복수형으로) - articles
```

1. `admin.py`

   > 관리자 페이지

2. **`models.py`**

   > 앱에서 사용하는 Model(Database)를 정의하는 곳.

3. **`views.py`**

   > 중간 관리자 역할.



## 3. 초기설정

1. `setting.py`

   > 웹사이트의 모든 설정 포함, 어플리케이션이 등록되고 파일들의 위치, DB의 세부 사항 보안 등

   1. 앱을 생성하면 앱이랑 플젝이 동일선상에 만들어져있음. 하나의 프로젝트는 여러 어플리케이션을 가지고 있는데 장고는 어플리케이션이 만들어져도 프로젝트 입장에서는 어플리케이션이 만들어졌는지 알수가 없어서 프로젝트에 **등록**해주는 작업 필요.

      - `INSTALLED_APPS`에 있는 건 장고가 구동되는데 기본적으로 필요한 앱들임.

      - 어플리케이션 이름을 등록시켜주면 된다.

        ```python
        # settings.py
        
        INSTALLED_APPS = [
        	'articles', <-- 내가 만든 어플리케이션 이름 넣어주기
            'django.contrib.admin',
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.messages',
            'django.contrib.staticfiles',
        ]
        ```

        >**INSTALLED_APPS의 app order**
        >
        >```python
        >INSTALLED_APPS = [
        >    
        >    # 1. local apps
        >    'articles',
        >
        >    # 2. Third party apps
        >    'haystack',
        >
        >    # 3. Django apps
        >    'django.contrib.admin',
        >    'django.contrib.auth',
        >    'django.contrib.contenttypes',
        >    'django.contrib.sessions',
        >    'django.contrib.sites',
        >
        >]
        >```
      
   2. 언어, 시간 바꾸기

       ```python
       LANGUAGE_CODE = 'ko-kr'

       TIME_ZONE = 'Asia/Seoul'
       ```

2. **`urls.py`**

	> 사용자의 요청을 가장 먼저 만나는 곳. 사이트의 내부  연결 지정
	



<span style="color:red">**APP의 이름은 복수형으로**</span>

<span style="color:red">**APP 생성 후 등록** = startapp으로 app 만든 다음에 setting에 추가!!</span>



---



## MTV 패턴

 ![image-20210310230148318](Django 정리.assets/image-20210310230148318.png)

**model**

- 응용프로그램의 데이터 구조를 정의하고 데이터베이스의 기록을 관리(추가, 수정, 삭제)

**template**

- 파일의 구조나 레이아웃을 정의
- 실제 내용을 보여주는 데 사용 (presentation)

**view**

- HTTP 요청을 수신하고 HTTP 응답을 반환
- Model을 통해 요청을 충족시키는데 필요한 데이터에 접근
- 그리고 탬플릿에게 응답의 서식 설정을 맡김



---



## 요청과 응답

> **서버가 구동이 되었으니까 이제 요청과 응답의 사이클 진행**



1. **`urls.py`**

   * 요청을 가장 먼저 받는 곳

   * 요청을 알맞은 `views.py`의 함수로 전달 해줘야함

   ```python
   # urls.py
   
   from django.contrib import admin
   from django.urls import path
   from articles import views - 다른 위치에 있으니까 경로도 알려주기
   
   urlpatterns = [
       path('admin/', admin.site.urls),
       path('index/', views.index),
   ]
   ```

   1. `'admin/'` 얘는 주소를 의미.  

      서버를 켜서 주소 뒤에 `/admin`이라고 넣어주면 해당 페이지로 이동

   2. 메인 페이지의 주소는 일반적으로 `index` 라고 지정.

   3. `\path`의 두번째 인자는 만약 url주소가 index로 요청이 들어왔을 때, 어떤 view 함수를 실행시킬건지? 

      따라서 메인 페이지를 보여주는 views.py 에 있는 함수를 호출을 할거고 그 함수가 지금 views에 없으니까 views.py로 이동해서 함수 만들어주기. (index라는 함수를 만들어줄 예정)

   4. 만들어진 함수 이름을 두번째 인자로 넣기 (`views.index`)

       = views 안에 있는 인덱스라는 함수로 연결

      (다른 위치에 있으니까 경로도 알려주기 - `from articles import views`)

      

      ***사용자의 요청이 index라는 주소값으로 들어온다면 urls.py가 그 url을 인식해서 views.index이걸 호출할거야 라는 의미***

      

2. **`views.py`**

   * HTTP 요청을 수신하고 HTTP 응답을 반환하는 함수 작성

   ```python
   # views.py
   
   from django.shortcuts import render
   
   def index(request): # view 함수의 첫번째 인자는 반드시 request
       return render(request, 'index.html') # 랜더도 request 첫번째 인자로 무조건!
   ```

   1. `urls.py`에서 index라는 주소가 들어왔고 views.py에 있는 index라는 함수와 연결했음.

   2. 어디 사이트를 들어가던 우리가 보는 것은 결국 html문서 하나. 따라서 views에 있는 함수가 데이터들을 조합해 하나의 완성된 템플릿을 만들어야하는데 조합할 데이터가 없으니까 하나의 문서를 보여주고 싶다.(html이 필요하다는 의미)  = `render` : 잘 포장해서 보여줄게, 

   3. `return`의 두번째 인자로는 **우리가 보여줄 페이지가 작성될 템플릿 경로 작성**

      템플릿이 없으니까 템플릿 만들어주러 가야함.

   4. 만들고 와서 장고는 templates라는 경로는 이미 알고있어서 templates라는 폴더 하위에 있는 것들만 두번째 인자로 넣어주면 됨. ex) `'index.html'`

   

3. **`'templates/~~~~~~~.html'`**

   * `views.py`에서 지정한 `index.html` 파일을 만들기
   * Django에서 template이라고 부르는 HTML 파일은 기본적으로 **app 폴더안의 templates 폴더 안에 위치**한다. 
   * 꼭 **`s`** 붙이기!!
   * 화면에 표시될 내용 적기

   ```html
   # index.html
   # ! + tab => 자동완성
   
   <!DOCTYPE html>
   <html lang="en">
   <head>
     <meta charset="UTF-8">
     <meta http-equiv="X-UA-Compatible" content="IE=edge">
     <meta name="viewport" content="width=device-width, initial-scale=1.0">
     <title>Document</title>
   </head>
   <body>
     <h1>만나서 반가워요</h1>
     <a href="/greeting/">greeting</a>
     <a href="/dinner/">dinner</a>
   </body>
   </html>
   ```

    ![image-20210311024132230](Django 정리.assets/image-20210311024132230.png)

---



## DTL

>  Django Template Language 
>
> 장고 템플릿 내부에서 사용하는 언어
>
> https://docs.djangoproject.com/en/3.1/ref/templates/language/



* Variable

  * **{{ variable }}**
  * render()를 이용해서 views.py에서 정의한 변수를 template 파일로 넘겨줌
  * dot(.)를 사용해서 변수 속성에 접근
  * 딕셔너리 형태로 넘겨주며, key에 해당하는 문자열이 template에서 사용 가능한 변수명이 된다.

  ```python
  # views.py
  
  from django.shortcuts import render
  
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
  ```

  ```django
  # 'greeting.html'
  
  <!DOCTYPE html>
  <html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
  </head>
  <body>
    
    <h1>안녕하세요 저는 {{ info.name }} 입니다. </h1> - info라는 딕셔너리 안에 name이라는 키 값 존재
    
    <p>제가 좋아하는 음식은 {{ foods }}입니다.</p> - 리스트 그대로 넘어옴 
    
    <p>제가 가장 좋아하는 음식은 {{ foods.0 }}입니다.</p> - 인덱스로 접근
  </body>
  </html>
  ```

   ![image-20210311024112952](Django 정리.assets/image-20210311024112952.png)

* Filter

  * **{{ variable|filter }}**

  * 수정하기 위해서 사용

    ex) {{ name|lower }} name이라는 변수를 모두 소문자로 출력

    ​		built-in template filter라는 문서에서 확인 가능

  ```python
  # views.py
  
  from django.shortcuts import render
  
  def dinner(request):
      foods=['족발','피자','햄버거','치킨']
      pick=random.choice(foods)
      context = {
          'pick':pick,
          'foods': foods,
      }
      return render(request, 'dinner.html', context)
  ```

  ```django
  # 'dinner.html'
  
  <!DOCTYPE html>
  <html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
  </head>
  <body>
    <h1>오늘 저녁은 {{ pick }}</h1>
    <p>{{ pick }}은 {{ pick|length }}글자</p>
  </body>
  </html>
  ```

  django built in filters라고 검색하면 많음

  https://docs.djangoproject.com/ko/3.1/ref/templates/builtins/#built-in-template-tags-and-filters

  

* Tags

  * **{ % tag % }**
  * 출력 텍스트를 만들거나, 반복 또는 논리를 수행하여 제어 흐름을 만드는 등 변수보다 복잡한 일들을 수행

  ```django
  # dinner.html
  
    {% comment %} tag 쓰기 {% endcomment %}
  
    <p>메뉴판</p>
    <ul>
      {% for food in foods %}  - 얘는 tag
        <li>{{ food }}</li> - 얘는 변수 
      {% endfor %}
    </ul>
  
  ```

  

* Comments

  * **{ # ~~~~~~~~ # }**
  * django template에서 줄의 **주석**을 표현하기 위해 사용
  * 여러 줄 주석은 **{% comment %}~~~~{% endcomment %}** 사이에 입력
  
  ```django
  # dinner.html
  
    {# 이것은 주석입니다 #}
    {% comment  %}
      <p>1</p>
      <p>2</p>
      <p>3</p>
    {% endcomment %}
  ```
  
   ![image-20210311024207888](Django 정리.assets/image-20210311024207888.png)

---



## Template Inheritance

* 템플릿 상속은 기본적으로 코드의 재사용성에 초점을 맞춤

* 템플릿 상속을 사용하면 사이트의 모든 공통 요소를 포함하고, 하위 템플릿이 재정의(override) 할 수있는 블록을 정의하는 기본 “skeleton” 템플릿을 만들 수 있음

* 지금까지는 html을 앱에 작성했는데 베이스라는건 모든 앱에도 다 적용되길 원하니까 앱이 들고있는거보다는 프로젝트가 들고있는게 더 효율적

* 따라서 프로젝트에 templates라는 폴더 만들어서 `base.html `만들어주기.

  ```django
  # firstpjt/base.html
  
  <!DOCTYPE html>
  <html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-BmbxuPwQa2lc/FVzBcNJ7UAyJxM6wuqIj61tLrc4wSX0szH/Ev+nYRRuWlolflfl" crossorigin="anonymous">
    <title>Document</title>
  </head>
  <body>
    <nav class="navbar navbar-light bg-light">
      <div class="container-fluid">
        <a class="navbar-brand" href="#">Navbar</a>
      </div>
    </nav>
  
    <div class="container">
      {% block content %}
      	자식 템플릿은 이 안에서 작성하면됨
      {% endblock  %}  
    </div>
  
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/js/bootstrap.bundle.min.js" integrity="sha384-b5kHyXgcpbZJO/tY9Ul7kGkf1S0CWuKcCD38l8YkeH8z8QjE0GmW1gYU5S9FOnJ0" crossorigin="anonymous"></script>
  </body>
  </html>
  ```

  * `block` + `tab`  : 이 부분을 자식에게 넣어줌. 자식 템플릿은 필요한 부분만 가져가면 되니까 블럭에도 이름을 만들어준다. 여기선 content

  * https://getbootstrap.com/docs/5.0/getting-started/introduction/

    부트스트랩 cdn 들고오기 css랑 js

  ```django
  # index.html
  # 위의 index.html이 base.html을 상속 받아오면서 이렇게 변함.
  # 이건 코드 맨 위에서 정의되어야 함
  
  {% extends 'base.html' %}
  
  {% block content %}
    <h1>만나서 반가워요</h1>
    <a href="/greeting/">greeting</a>
    <a href="/dinner/">dinner</a>
  {% endblock  %}
  ```

  *근데 templates 뒤에 경로를 이미 알고있다는 건 app_name/templates/이 뒤의 경로를 알고 있는거여서 base.html은 프로젝트의 templates 폴더에 저장되어 있으니까 django가 경로를 알지를 못함.* -> 새로운 경로에도 templates가  있다는 것을 알려줘야함 -> settings.py로 이동

  ```python
  # settings.py
  
  TEMPLATES = [
      {
          ...,
          'DIRS': [BASE_DIR / 'firstpjt' / 'templates'],
  ...				
  ]
  ```

   ![image-20210311031957317](Django 정리.assets/image-20210311031957317.png)

* **`extends` tag**

  - 자식(하위)템플릿이 부모 템플릿을 확장한다는 것을 알림
  - 반드시 템플릿 **최상단**에 위치해야 함(== 템플릿의 첫번째 템플릿 태그여야 함)
    - 즉, 2개 이상 사용할 수 없음

  

* **`block` tag**

  - 하위 템플릿에서 재지정(overriden)할 수 있는 블록을 정의

  - 하위 템플릿이 채울 수 있는 공간

  - 가독성을 높이기 위해 선택적으로 `{% endblock %}` 태그에 이름 지정

    ```django
    {% block content %}
    {% endblock content %}
    ```

  

---



## HTML form

**HTML `<form>` element**

- 웹에서 사용자 정보를 입력하는 여러 방식(text, button, checkbox, file, hidden, image, password, radio, reset, submit)을 제공하고, 사용자로부터 할당된 데이터를 서버로 전송하는 역할을 담당
- 핵심 속성
  - action : 입력 데이터가 전송될 URL 지정 = 어디로?
  - method : 입력 데이터 전달 방식 지정 



**HTML `<input>` element**

* 사용자로부터 데이터를 입력 받기 위해 사용
* `type` 속성에 따라 동작 방식이 달라짐
* 핵심 속성
  - **name**
  - 중복 가능, 양식을 제출했을 때 name이라는 이름에 설정된 값을 넘겨서 값을 가져올 수 있음
  - 주요 용도는 GET/POST 방식으로 서버에 전달하는 파라미터**(name 은 key , value 는 value)**로 `?key=value&key=value` 형태로 전달



---



## HTTP request methods

**GET**

- 검색은 결국 결과를 얻고 싶은거 
- 서버로부터 **정보를 조회**하는 데 사용
- 데이터를 가져올 때만 사용해야 함
- 데이터를 서버로 전송할 때 body가 아닌 **Query String Parameters**를 통해 전송





---

**예시문제 - throw & catch** 

이제부터 할건 데이터를 보내고 서버에서 데이터 받고 그 받은걸 다시 그대로 넘겨주기!!

예를들어 안녕이라고 보내면 장고가 안녕을 받아서 다른 페이지에 안녕을 보여주기



<작성 순서>

1. urls.py 부터 작성.

2. view 함수는 데이터 받을 템플릿 출력하는 함수,  앞에서 만들어진 데이터를 (보내진 데이터) 받는 함수. 그래서 form 태그가 있는 즉 데이터를 받는 템플릿 하나 결과를 보여줄 템플릿 하나

   *즉 함수도 두개 템플릿도 두개 필요!!*

   

**데이터 받을 템플릿 출력하는 함수 = throw** 

1. urls.py

   > 프로젝트 폴더의 urls.py로 이동

   보내는거 만들기

   ```python
   # urls.py
   
   from django.contrib import admin
   from django.urls import path
   from articles import views
   
   urlpatterns = [
       path('throw/', views.throw),
   ]
   ```

2. articles/views.py

   > 앱 폴더의 views.py로 이동

   ```python
   # views.py
   # 사용자한테 입력을 받을 템플릿을 출력해주는 애. 그냥 템플릿으로 이동하게만 만들어주면 될 듯?
   
   from django.shortcuts import render
   
   def throw(requset):
       return render(request, 'throw.html')
   ```

3. articles/templates/throw.html

   ```django
   사용자의 데이터를 받고 전송하기 위해서는 HTML의 form 태그가 그 역할을 해주니까 form태그 넣어주기.
   
   
   {% extends 'base.html' %}
   
   {% block content %}
     <h1>THROW</h1>
     사용자의 데이터를 받고 전송
     method는 필수인데 디폴트는 get이지만 명시해주기 action : 캐치로 보낸다. 주소 넣어주기
     <form action="/catch/" method='GET'>
       라벨태그는 id와 연결
       <label for="message">Throw: </label>
   	사용자의 입력을 받는 태그
       여기에 입력하는 값은 value 인데 서버의 입장에선 value에 바로 접근할 수 없으니까 name=key값을 줘야한다. 꼭!!
       <input type="text" name='message' id='message'>
       제출 하기 만들기 (제출하기는 form의 바깥쪽에 있으면 안됨.)
       <input type="submit">
     </form>
   
   {% endblock  %}
   
   ```

    ![image-20210311183049454](Django 정리.assets/image-20210311183049454.png) ![image-20210311183151256](Django 정리.assets/image-20210311183151256.png)

   입력을 하고 제출을 하면 위의 주소값이 바뀜. 내가 name을 message로 줬으니까
    http://127.0.0.1:8000/throw/?message=ㅎㅇㅎㅎㅇㅎㅇ 이런식!
   보낼 주소가 없기때문에 페이지가 전환이 되진 않음
   ==> 데이터를 받아서 보낼 view는 완성.

   ​		보내진 데이터를 다시 받아서 클라이언트로 보낼 view 필요! (catch)

   

**보내진 데이터를 다시 받아서 클라이언트로 보낼 view 필요! (catch)**

1. urls.py

   > 프로젝트 폴더의 urls.py로 이동

   보내는거 만들기

   ```python
   # urls.py
   
   urlpatterns = [
       path('catch/', views.catch),
   ]
   ```

2. articles/views.py

   > 앱 폴더의 views.py로 이동

   ```python
   # views.py
   # 얘는 throw에서 보낸 데이터를 받아서 catch에서 출력을 해줘야함
   # request의 GET에 접근을 해야 아까 제출한거에 접근 가능
   
   def catch(request):
       message = request.GET
       print(message) -> <QueryDict: {'message': ['안녕']}> 이런식으로 나옴
       ---------------------- 따라서 안녕까지 접근을 해야하니까 위처럼 쓰지 말고 딕셔너리니까 get(key)쓰기---
       message = request.GET.get('message')
       # 즉 request에 있는 GET에 딕셔너리가 하나 있는데 그 값이 message인 값을 가져오기 그래서 이걸 context에 담아서 catch.html에 넘겨주기
           context = {
           'message':message,
       }
       return render(request, 'catch.html', context)
   ```

3. articles/templates/catch.html

   ```django
   {% extends 'base.html' %}
   
   {% block content %}
     <h1>CATCH</h1>
     <h2>{{ message }}도착 완료</h2>
   {% endblock  %}
   ```

    ![image-20210311190052196](Django 정리.assets/image-20210311190052196.png) ![image-20210311190134627](Django 정리.assets/image-20210311190134627.png)



---

<span style="color:blue">**파일바꾸기**</span>

## URLs

> 웹 어플리케이션은 URL을 통한 클라이언트의 요청에서부터 시작



### URL mapping

만약 앱에 뷰함수가 많아지만 path가 늘어날텐데, 앱 또한 많아진다면 프로젝트의 urls.py에서 모든걸 다 관리하기는 쫌 문제

따라서 각 app에 urls.py를 만들어줄거임. 각 앱이 자기의 url을 가져가도록!

```bash
$ python manage.py startapp pages
```

```
# articles, pages : app
# firstpjt : 플젝이름

articles/
	urls.py
	views.py
pages/
	urls.py
	views.py
firstpjt/
	urls.py
	settings.py
```

 이렇게 앱(pages)을 하나 더 만들어줬으면 setting.py에 가서 pages 추가, 

```python
INSTALLED_APPS = [
    'articles',
    'pages',
    ...,
]
```

 firstpjt/urls.py에 들어가서 `from pages import views` 얘를 추가해주려고 보니까 `from articles import views`이미 얘가 존재하는중.. 그래서 이렇게 하지말고 저거 두개 views.py에서 지우고

```python
# firstpjt/urls.py
# 이거만 남은 상태
# 어드민만 남겨놓고 원래 있던 path들은 예전에 있던 articles로 다 옮겨줌

from django.contrib import admin
from django.urls import path

urlpatterns = [
    # 'admin/' 얘는 주소를 의미. 서버를 켜서 주소 뒤에 /admin이라고 넣어주면 해당 페이지로 이동
    path('admin/', admin.site.urls),   
]
```

앱들의 urls.py에 들어가서

```python
# articles/urls.py

from django.urls import path
from . import views - 같은 위치에 있으니까 현재 디렉토리에서 views.py를 가져올거야

urlpatterns = [
    path('index/', views.index),
    path('greeting/', views.greeting),
    path('dinner/', views.dinner),
    path('throw/', views.throw),
    path('catch/', views.catch),
]
```

```python
# pages/urls.py

from django.urls import path

urlpatterns=[
    
]
```

그럼 지금 firstpjt/urls.py - articles/urls.py

​											- pages/urls.py  이렇게 두개로 나뉨

여기서 프로젝트의 url의 역할은 처음 요청이 들어왔을때 articles로 보낼지, pages로 보낼지를 판단해주는거!

따라서 마지막으로 이런식으로 수정해야한다.

**`include()`**

- 다른 URLconf(app1/urls.py)들을 참조할 수 있도록 도움
- 함수 include()를 만나게 되면, URL의 그 시점까지 일치하는 부분을 잘라내고, 남은 문자열 부분을 후속 처리를 위해 include된 URLconf로 전달

```python
# firstpjt/urls.py
# 이거만 남은 상태
# 어드민만 남겨놓고 원래 있던 path들은 예전에 있던 articles로 다 옮겨줌

from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    # 'admin/' 얘는 주소를 의미. 서버를 켜서 주소 뒤에 /admin이라고 넣어주면 해당 페이지로 이동
    path('admin/', admin.site.urls),
    # 일반적으로 주소는 그 앱의 이름으로 함
    # url이 articles로 시작하는 url로 들어오면 articles/url로 넘어가야함. = include 추가
    path('articles/', include('articles.urls')),
    path('pages/', include('pages.urls')),
]
```

![image-20210311194529303](Django 정리.assets/image-20210311194529303.png) ![image-20210311194626345](Django 정리.assets/image-20210311194626345.png)

이렇게 url을 분리시켜 줬으니까 바로 index라고 하면 안되고 articles에 index라는 함수를 넣어줬으니까 articles/index라고 접근해야함.
articles : firstpjt/urls.py에서 판단해서 articles/urls.py로 보내야겠다!!
index : articles(app)로 옮겨가서 그 안에서 매칭되는 index함수 찾기



### Variable routing

- 동적 라우팅
  
  - 사용자의 입력을 통해 계속 바뀌는 걸 만들고 싶음
  - 주소 자체를 변수처럼 사용해서 동적으로 주소를 만드는 것]
  
  ```python
  # articles/urls.py
  
  urlpatterns = [
      ...,
      # <> : 주소의 이 부분을 마음대로 바꿀 수 있다. 단 타입이 str
      path('hello/<str:name>/', views.hello),
  ]
  ```
  
  ```python
  # articles/views.py
  
  # 동적 변수 name이 두번째 인자로 들어옴
  def hello(request, name):
      context = {
          'name': name,
      }
      return render(request, 'hello.html', context)
  ```
  
  ```django
  <!-- articles/hello.html -->
  
  {% extends 'base.html' %}
  
  {% block content %}
    <h1>만나서 반가워요 {{ name }}님!</h1>
  {% endblock %}
  ```
  
   ![image-20210311200244006](Django 정리.assets/image-20210311200244006.png)

	### Naming URL patterns

* Django는 URL에 이름을 지정하는 방법을 제공하므로써 뷰 함수와 템플릿에서 특정 주소를 쉽게 참조할 수 있도록 도움

앱을 분리한 상태임. 
근데 index페이지에서 greeting페이지로 넘어가기 위해 클릭을 하면 원래 `<a href="/greeting/">greeting</a>`이런식으로 a태그가 들어있어서 greeting을 찾아가야하는데 articles/greeting에 이렇게 들어가야하니까 안됨. 
그래서 greeting의 html로 들어가서 action을 'articles/greeting'으로 바꾸고, index의 a태그를 또 '/articles/greeting/'이렇게 바꿔야 하는데 너무 많음. - 하드코딩

그래서 **처음에 작성할 때부터 urls.py에서 path에 이름을 정해줘서** `<a href="{% url 'greeting' %}">greeting</a>` 이렇게 이름으로 넘겨주면 이동 가능



```python
# articles/urls.py

urlpatterns = [
    path('index/', views.index, name='index'),
    path('greeting/', views.greeting, name='greeting'),
    path('dinner/', views.dinner, name='dinner'),
    path('throw/', views.throw, name='throw'),
    path('catch/', views.catch, name='catch'),
    path('hello/<str:name>/', views.hello, name='hello'),
]
```

**url tag 사용하기**

```django
<!-- index.html -->

{% extends 'base.html' %}

{% block content %}
  <h1>만나서 반가워요!</h1>
  <a href="{% url 'greeting' %}">greeting</a>
  <a href="{% url 'dinner' %}">dinner</a>
  <a href="{% url 'throw' %}">throw</a>
{% endblock %}
```



그럼 만약에 두번째 앱에서도 greeting이 필요할땐 어떻게해??


