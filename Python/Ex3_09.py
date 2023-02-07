numbers = [2, 3, 5, 7, 11, 13, 17, 19]

# 리스트 뒤집기
for i in range(len(numbers) // 2):
    tmp = numbers[i]
    numbers[i] = numbers[-i - 1]
    numbers[-i - 1] = tmp

print("뒤집어진 리스트: " + str(numbers))