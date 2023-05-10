import random #random 함수 사용을 위해 적는 코드 (굳이 random 함수를 사용하지 않고 1~4반 형식으로 두어도 좋습니다)

munga = sub1 = str(input('자신이 문과라면 문과 이과라면 이과 라고 입력하세요'))#
sub1 = str(input('자신이 일본어를 들으면 일본어 아니면 중국어를 입력하세요'))

#반 배정기
if (munga =='문과' and sub1 =='일본어'): #munga가 문과와 일치하고 sub1가 일본어인 경우 실행
    ban = random.randrange(1,4)# ban을 1이상 4 미만의 값으로 설정
    print(ban,'반입니다!')
elif (munga == '문과' and sub1 =='중국어'):#munga가 문과와 일치하고 sub1가 중국어인 경우 실행
    ban = 4
    print(ban,'반입니다!')
elif (munga =='이과' and sub1 =='일본어'):#munga가 이과와 일치하고 sub1가 일본어인 경우 실행
    ban = random.randrange(5,9)# ban을 5이상 9 미만의 값으로 설정
    print(ban,'반입니다!')
elif (munga =='이과' and sub1 =='중국어'):#munga가 이과와 일치하고 sub1가 중국어인 경우 실행
    ban = 9
    print(ban,'반입니다!')
else:
    print('잘못 입력하셨습니다!')


#예상 난이도 ★★★☆☆(변수 확인 과정이 그렇게까지 어렵지는 않음)
 