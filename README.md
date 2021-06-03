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
- conda 4.10.1
- vs Code로 개발 진행 
<br></br>

#### 1. Install Django Framework (Terminal)
```
pip install django
```
#### 2. Module 설치 (Terminal)
```
pip install wordcloud
```

### Error!
- seaborn & scipy module이 서로 충돌하기 때문!
- module 지웠다 다시 깔아줄 것 
```
pip uninstall scipy
pip uninstall seaborn
```
```
pip install scipy
pip install seaborn
```

#### 3. 실행 (Terminal)
- manage.py가 있는 폴더에서 명령어 실행하기
```
python manage.py runserver
```


