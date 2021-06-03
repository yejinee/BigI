from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import io
import urllib, base64
from urllib.parse import urlparse
import re 
import pandas as pd
import seaborn as sns



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
        bcnt,blev,bage=basicinfo(book)
        uni=unigram(book)

        data = { 'wordimage': wordimage ,'bcnt':bcnt, 'uni': uni,'blev':blev,'bage':bage} 
        return render(request, 'resultpage.html', data)


def word_cloud(book):
    # wordcloud추출

    spwords=set(STOPWORDS) # 제외할 단어
    wc = WordCloud(stopwords=spwords,background_color="white", contour_width=2,width=1300, colormap='Set2', height=800,max_words=30, max_font_size=170,random_state=42)
    wc.generate(book)
    plt.imshow(wc, interpolation="bilinear")        
    plt.axis('off')
    fig=plt.gcf()
    image = io.BytesIO()
    plt.savefig(image, format='jpeg')
    image.seek(0)  # rewind the data
    string = base64.b64encode(image.read())

    image_64 = 'data:image/png;base64,' + urllib.parse.quote(string)
    #rimage = rescale(image_64, 700)
    return image_64


def basicinfo(book):
    # book의 문장 길이 
    bookcnt = book.split('.')
    cnt=len(bookcnt)
    score=-2.36730268
    lev=0
    age=""

    # level 계산 
    if 0<score<=1:
        lev=1
        age="8세 ~ 9세"
    elif -1<score<=0:
        lev=2
        age="10세 ~ 11세"
    elif -2<score<=-1:
        lev=3
        age="12세 ~ 13세"
    elif -3<score<=-2:
        lev=4
        age="14세 ~ 15세"
    else:
        lev=5
        age="16세 ~ 17세"

    return cnt,lev,age

def unigram(book):
    import string
    book_pred = pd.DataFrame()
    book_pred['word_clean'] = ""
    #filtering the unwanted symbols, spaces, ....etc
    to_replace_by_space = re.compile('[/(){}\[\]|@,;]')
    punctuation = re.compile(f'([{string.punctuation}“”¨«»®´·º½¾¿¡§£₤‘’])')
    bad_symbols = re.compile('[^0-9a-z #+_]')
    spwords=set(STOPWORDS) 


    book = book.lower() # lowercase text
    book = re.sub(punctuation, '',book)
    book = re.sub(to_replace_by_space, " ", book) # replace REPLACE_BY_SPACE_RE symbols by space in text
    book = re.sub(bad_symbols, "", book)         # delete symbols which are in BAD_SYMBOLS_RE from text
    book = " ".join([word for word in book.split(" ") if word not in spwords]) # delete stopwords from text
    book = re.sub(' +', ' ', book)

    
    book_clean=book.split()
    book_pred['word_clean'] =book_clean
    word_counter = book_pred['word_clean'].value_counts().rename_axis('word').reset_index(name='counts')

    plt.figure(figsize=(16, 8))
    ax = sns.barplot(x='counts', y='word', data=word_counter.loc[:20],linewidth=3)
    plt.title("Top 20 words", fontsize=22)
    plt.xlabel("Frequency", fontsize=16)
    plt.yticks(fontsize=13)
    plt.xticks(rotation=45, fontsize=13)
    plt.ylabel("")

    fig=plt.gcf()
    image = io.BytesIO()
    plt.savefig(image, format='jpeg')
    image.seek(0)  # rewind the data
    string = base64.b64encode(image.read())

    image_64 = 'data:image/png;base64,' + urllib.parse.quote(string)
    #rimage = rescale(image_64, 700)
    return image_64





