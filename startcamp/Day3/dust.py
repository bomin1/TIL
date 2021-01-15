# 공공 데이터 API 활용 실습 (대기오염정보)

# 1. 필요한 라이브러리 import 하기
import requests


# 2. API URL 및 KEY값 확인
key = 'wPHG%2BGoFaCBGzzzm%2BEqG9R3WSjuyke3SafU5unUgBHJ7XLb7DwEnjcna59hpmBsqInb9Z4CIraNICKbq6rC6rQ%3D%3D'
url = f'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey={key}&sidoName=광주&returnType=json'
response = requests.get(url).json()



# # 3. 요청 및 응답값 확인
city = response['response']['body']['items'][1]['sidoName']
station = response['response']['body']['items'][1]['stationName']
val = response['response']['body']['items'][1]['pm10Value']


# # 4. 최종 출력 문자열
# # '==의 미세먼지 농도는 ==입니다. (측정소: ===) '

text = (f'{city}의 미세먼지 농도는 {val}입니다. (측정소: {station})')

#5. 텔레그램 메시지 전송 
token = '1518258838:AAFM1gNfAS-OCvyiOZXdGCJb8o574ZSfSfQ'
chat_id = '1597895806'
telegram_url = f'https://api.telegram.org/bot{token}/sendMessage?chat_id = {chat_id}&text\{text}'

requests.get(telegram_url)