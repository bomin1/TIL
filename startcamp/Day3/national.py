import requests, pprint

#  API 요청 url 확인 + 필요한 데이터 건네주기
name = 'bomin'

url = f'https://api.nationalize.io/?name={name}'


# URL로 요청 보내기
response = requests.get(url).json()
pprint.pprint(response)

# 응답결과 확인 후 정보 추출하기
name = response['name']
country = response['country'][0]['country_id']

pro = round(response['country'][0]['probability']*100, 2)

print(f'{name}의 국적은 {pro}% 확률로 {country}입니다.')