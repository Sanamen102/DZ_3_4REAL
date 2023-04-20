num = int(input("Введите число: "))

if num > 1:
    for i in range(2,num):
        if (num % i) == 0:
            print("Составное")
            break
    else:
        print("Простое")
else:
    print("Составное")