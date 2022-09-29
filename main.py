from random import randint

N = int(input("\nВведите количество чисел (N): "))
dir = input("Введите направление сортировки\n0 - по убыванию, 1 - по возрастанию: ")
a = []
for i in range(N):
    a.append(randint(1, 99))
print(a)

for i in range(N - 1):
    for j in range(N - i - 1):
        if dir == '0':
            if a[j] < a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
        elif dir == '1':
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
        else:
            print("Некорректный ввод!")
print(a)
