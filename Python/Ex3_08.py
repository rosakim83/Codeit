#피타고라스 삼조
for a in range(1, 401):
    for b in range(1, 401):
        c = 400 - a - b
        if a * a + b * b == c * c and a < b < c:
            print(a * b * c)