import requests
from bs4 import BeautifulSoup

# 웹 페이지에 접속하여 HTML 소스 코드 가져오기
url = "https://sports.news.naver.com/wfootball/record/index"
response = requests.get(url)
html_source = response.text

# BeautifulSoup을 사용하여 HTML 파싱
soup = BeautifulSoup(html_source, 'html.parser')

# 원하는 요소 선택하기
table = soup.find_all('td', attrs={"class": "num best"})

print(table)
