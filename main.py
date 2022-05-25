# Пользователь задаёт две строки. Определить количество вхождений одной строки в другой.
string1 = input('Задайте первую строку: ').lower()
string2 = input('Задайте вторую строку: ').lower()
count = 0
if (len(string1) > len(string2)):
    count_in_string = string1.count(string2)
else:
    count_in_string = string2.count(string1)
print(f'Количество вхождений {count_in_string}')