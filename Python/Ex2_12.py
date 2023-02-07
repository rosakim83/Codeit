year = 1988
money = 50000000

while year < 2016:
    money *= 1.12
    year += 1

if money >= 1100000000:
    print(f"{round(money) - 1100000000}원 차이로 동일 아저씨 말씀이 맞습니다.")
else:
    print(f"{1100000000 - round(money)}원 차이로 미란 아주머니 말씀이 맞습니다.")