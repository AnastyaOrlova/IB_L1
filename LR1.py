import time

password = "123456"
L = len(password)
N = 10
i = 0
M = pow(N, L)
print("Длина пароля, L =", L)
print("Мощность алфавита, N =", N)
print("Количество возможных комбинаций, М =", M)

while True:
    password_inp = input("Введите пароль: ")
    if (password == password_inp):
        print("Выполнен вход")
        break
    else:
        print("Неверный пароль")
        i += 1
        if i == 3:
            time.sleep(5)
