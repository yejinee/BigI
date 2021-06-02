from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
import string
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import io
import urllib, base64
from urllib.parse import urlparse

# Create your views here.
def mainpage(request):
    return render(request, 'index.html')
"""

def resultpage(request):
    return render(request, 'resultpage.html')
"""
def get_post(request): 
    if request.method == 'GET': 
        urltext = request.GET['urltext'] 
        link1=requests.get(urltext)
        mlist=BeautifulSoup(link1.content,"html.parser") # html.content를 가져오기 
        cont = mlist.find("div",{"class":"jumbotron"}) # 원하는 태그를 선택 (개발자 도구 참조 )
        book=cont.text 
        data = { 'book': book } 
        return render(request, 'resultpage.html', data)
    elif request.method == 'POST':
        urltext = request.POST['urltext'] 
        # 크롤링 해오기 (링크)
        link1=requests.get(urltext)
        mlist=BeautifulSoup(link1.content,"html.parser") # html.content를 가져오기 
        cont = mlist.find("div",{"class":"jumbotron"}) # 원하는 태그를 선택 (개발자 도구 참조 )
        book=cont.text 
        wordimage = word_cloud(book)

        data = { 'wordimage': wordimage } 
        return render(request, 'resultpage.html', data)


def word_cloud(book):
    # 그래프 출력 되는지
    spwords=set(STOPWORDS) # 제외할 단어
    wc = WordCloud(stopwords=spwords,background_color="black", contour_width=2,width=1000, colormap='Set2', height=750,max_words=30, max_font_size=170,random_state=42)
    wc.generate(book)
    plt.imshow(wc, interpolation="bilinear")        
    plt.axis('off')
    fig=plt.gcf()
    image = io.BytesIO()
    plt.savefig(image, format='png')
    image.seek(0)  # rewind the data
    string = base64.b64encode(image.read())

    image_64 = 'data:image/png;base64,' + urllib.parse.quote(string)
    
    return image_64 

