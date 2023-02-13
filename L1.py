import time

password = input("Введите пароль не менее 8 символов:\n")
i = 0
while True:
    for i in range (5):
        L = len(password)
        N = len(set(password))
        if L >= 8:
            print("Длина пароля, L =", L)
            print("Мощность алфавита, N =", N)
            M = pow(N, L)
            print("Количество возможных комбинаций, М =", M)
            break
        else:
            password = input("Мало символов, повторите ввод пароля:\n")

    time.sleep(15)