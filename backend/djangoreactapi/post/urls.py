## 경로 설정해주는 파일
from django.urls import path # path 함수를 이용하기 위해서 선언
from . import views     # from 옆에 .(점)은 현재 폴더(app)를 의미, 현재 폴더에 views.py 가져옴

app_name='post'
urlpatterns = [ 
path('', views.mainpage),
path('resultpage/', views.get_post, name='resultpage'),
  ]
# post -> parameter 로 전송하는거 
# main -> resultpage