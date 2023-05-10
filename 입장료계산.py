
#입장료 계산기
age = input('나이') #받은 값을 age에 저장, int(input('나이'))를 하지 않는 이유 input의 값이 문자열인데 int형으로 변환하려고 하면 오류가 생기기 때문!
if age.isdigit(): #age가 숫자인지 확인 isdigit(): 값이 숫자 형태이면 True 반환
    age = int(age) #age를 숫자형으로 설정  
    fee = 10000
    #age가 65를 초과하면 입장료의 20%,13 미만이면 50% 할인된 값을 fee에 할당
    if age > 65:
        fee=fee*0.8
    elif age<13:
        fee=fee*0.5
    print(f"입장료는 {fee}원입니다.")
else:
    print("나이는 숫자로 입력해주세요.")#숫자가 아닌경우 실행



 #예상 난이도 ★★☆☆☆(쉬운 논리 및 적은 내용)



