i = 1
cnt = 0
while i <= 120:
    if 120 % i == 0:
        print(i)
        cnt += 1
    i += 1
print(f"120의 약수는 총 {cnt}개입니다.")