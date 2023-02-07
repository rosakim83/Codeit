cnt = 1
previous = 0
current = 1
while cnt <= 50:
    print(current)
    temp = previous
    previous = current
    current += temp
    cnt += 1