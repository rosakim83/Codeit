def calculate_change(payment, cost):
    change = payment - cost
    print("50000원 지폐: {}장".format(change // 50000))
    change %= 50000
    print("10000원 지폐: {}장".format(change // 10000))
    change %= 10000
    print("5000원 지폐: {}장".format(change // 5000))
    change %= 5000
    print("1000원 지폐: {}장".format(change // 1000))


# 테스트 코드
calculate_change(100000, 33000)
print()
calculate_change(500000, 378000)