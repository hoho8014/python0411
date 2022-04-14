# web2.py
#웹서버에 요청
import urllib.request
#크롤링
from bs4 import BeautifulSoup

#파일 생성
f = open("c:\\work\\webtoon.txt", "wt", encoding="utf-8")
#수열함수로 페이지 번호 생성
for i in range(1,6):
    url = \
    "https://comic.naver.com/webtoon/list?titleId=20853&weekday=fri&page=" \
    + str(i)
    print(url)
    data = urllib.request.urlopen(url)
    #검색이 용이한 객체 
    soup = BeautifulSoup(data, "html.parser")
    cartoons = soup.find_all("td", class_="title")
    for item in cartoons:
        tag = item.find("a")
        print(tag.text.strip())
        f.write(tag.text.strip() + "\n")
f.close()