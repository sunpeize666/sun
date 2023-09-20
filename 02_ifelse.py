'''
    작성일 : 2023년 9월 20일
    작성자 : 학과 학번 이름
    설명 : 선택문 if~else
           정수를 입력받아 짝수인지 홀수인지 판단.
           
           짝수 = 2로 나눈 나머지가 0이다.   %, ==
           홀수 = 2로 나눈 나머지가 1이다. (0이 아니다.)  !=
'''
# 1. 정수를 입력 받는다.
num = int(input("정수 입력 : "))

# 2. 판단. - 판단의 기준은?
if num % 2 == 0 :
    print(num, "은(는) 짝수입니다.")
    print("{}은(는) 짝수입니다." .format(num))
    print(f"{num}은(는) 짝수입니다.")
else :
    print(num, "은(는) 홀수입니다.")
    print("{}은(는) 홀수입니다." .format(num))
    print(f"{num}은(는) 홀수입니다.")