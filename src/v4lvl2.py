#Уровень II. Задана строка текста на русском языке. Выписать все гласные буквы (заглавными, в том же порядке, как они следуют в строке, не повторяясь), которые входят в данный текст.

glasnieBukvi = ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е']

result = []

print('введите строку')
string = input()

for char in string:
    if char in glasnieBukvi and char.upper() not in result:
        result.append(char.upper())

print(result)