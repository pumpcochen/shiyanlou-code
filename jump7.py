for num in range(1, 101):
    if num % 7 == 0:
        continue
    if num % 10 != 0 and (num % 10) % 7 == 0:
        continue
    if  num // 10 != 0 and (num // 10) % 7 == 0:
        continue
    print(num)
