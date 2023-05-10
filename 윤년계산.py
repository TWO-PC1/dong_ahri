#윤년 계산기
year = input('현재년도를 입력하세요!')
if year.isdigit(): #year가 숫자인지 확인 isdigit(): 값이 숫자 형태이면 True 반환
    year = int(year)
    yunyear = year%4 # year를 4로 나눈뒤 나머지 계산 
    yunyear2 = year%100==0 and year%400!=0 #100으로는 나누어 떨어지지만 400으로는 나누어 떨어지지 않는경우를 만족하면 True 저장 

    #*중요* 100으로는 나누어 떨어지지만 400으로는 나누어 떨어지지 않는경우를 만족하면 평년이므로 yunyear2의 값을 반전시켜 사용하여야 함!

    if yunyear==0 and not yunyear2:#and 연산자를 통해 yunyear==0,not yunyear2이 모두 성립할때만 참이 된다.  연산자 not: 논리값을 반전시킴 ex) not True --> False,not False --> True
        print('윤년!')
    else:
        print('윤년이 아닙니다!')

else:
    print('양의 정수를 입력해주세요.')


#예상 난이도 ★★★★☆(윤년의 개념을 이해하고 코드에 적용시키는 과정이 어렵다고 생각함)
