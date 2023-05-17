#저번 시간 복습 내용입니다

money = input("돈을 넣어주세요: ")

if money.isdigit():
    money = int(money)
    if money >= 3000:
        print("택시를 타고 가세요")
    else:
        print("걸어가세요")