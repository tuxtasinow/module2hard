def find_password(n):
    result = ''
    # Перебираем все числа от 1 до n-1
    for i in range(1, n):
        for j in range(i+1, n):
            # Если число кратно сумме пары
            if n % (i + j) == 0:
                # Добавляем пару в строку
                result += str(i) + str(j)
    return result

# Пример использования
n = int(input("Введите число (от 3 до 20): "))
password = find_password(n)
print(f"Нужный пароль для числа {n}: {password}")
