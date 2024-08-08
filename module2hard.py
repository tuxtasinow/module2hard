def decoding(num):
    list_num = []
    for i in range(num):
        for j in range(i + 1, num):
            if (i + j) % num == 0:
                list_num.append(f'{i}{j}')
    return ''.join(list_num)


num = int(input('Введите число от 3 до 20: '))
result = decoding(num)
print(f'Пароль: {result}')