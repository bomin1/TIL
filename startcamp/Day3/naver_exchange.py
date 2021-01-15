# 웹 페이지 크롤링

import requests
from bs4 import BeautifulSoup

# 요청 보낼 주소 확인
url = 'https://finance.naver.com/marketindex/'

#requests로 요청을 보내고 응답 텍스트 받기
response = requests.get(url).text

# bs로 str을 구조화하여 데이터를 추출하기 쉬운 형태로 바꾸기
soup = BeautifulSoup(response, 'html.parser')
print(type(soup))

#경로를 건네주고 원하는 정보 추출하기
fin = soup.select_one('#exchangeList > li.on > a.head.usd > div > span.value').text

print(f"현재 원/달러 환율은 {fin}입니다.")