# 1. 기초 자료형

number = 3
# print(number)
# print(type(number))
string='문자열'
# print(string)
# print(type(string))
boolean = True
# print(boolean)
# print(type(boolean))

string_number = '3'
# print(int(string_number) + 5)

#2. f-string 문자열 안에 변수를 넣는다.
name='김창규'
# print(f'제 이름은 {name}입니다.')

#3. List
my_List = ['python', 'html', 'markdown']
# print(my_List[2])

# 4. Dictionary
age_dict = {'김' : 1, '박' : 2,}

# 딕셔너리 요소 접근
# print(age_dict['김'])

# 딕셔너리 요소 변경
age_dict['김'] = 20
# print(age_dict['김'])


# # 조건문
# n=10

# if n % 2 == 1:
#     print("홀수")
# else:
#     print("짝수")

#주어진 숫자가 양수인지 0인지 음수인지 파악해서 출력
# n=-5

# if n > 0:
#     print("양수")
# elif n == 0:
#     print("0")
# else:
#     print("음수")


#반복문
# numbers = [1, 2, 3]
# for numnber in numnbers:
#     print(number)


numbers = range(1, 10)
for number in numbers:
    if number % 2 == 1:
        print(f"숫자 {number}는 홀수입니다.")
    else:
        print(f"숫자 {number}는 짝수입니다.")