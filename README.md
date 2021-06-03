# Classification Text Level 
## < 교육용 텍스트 레벨 추천 서비스 >
<br></br>

### 서비스 개요
- 머신러닝을 통해 텍스트의 독해 필요 능력 수준 판독 알고리즘 개발 
- 텍스트 수준 판독 서비스 웹 서비스 제작
<br></br>

### 실행 
#### 0. Version Information
- python : 3.7.4
- vs Code로 개발 진행 
<br></br>

#### 1. Install Django Framework (Terminal)
```
pip install django
```
#### 2. Directory 지정 (Terminal)
```
mkdir backend
cd backend
django-admin startproject djangoreactapi . 
```

#### 3. API로 호출 시킬 APP 만들기 (Terminal)
- manage.py가 있는 폴더에서 실행
```
python manage.py startapp post
```

#### 4.Migrate 실행 (Terminal)
```
python manage.py migrate
```

#### 5.settings.py에 post 추가
```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'post',
]
```

#### 6. 실행 (Terminal)
```
python manage.py runserver
```

