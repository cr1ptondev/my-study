# # ---------------------------------------------------------------
# # Обучение на Python курс "Поколение Python": курс для начинающих
# # ---------------------------------------------------------------


# # ---------------------------------------------------------------
# # Тема урока: Числовые типы данных
# # ---------------------------------------------------------------

# Целые числа в Python представлены типом данных int (сокращение int происходит от слова integer). Для определения целого числа типа int используется последовательность цифр от 0 до 9.

# Явно указанное численное значение в коде программы называется целочисленным литералом. Когда Python встречает целочисленный литерал, он создает объект типа int, хранящий указанное значение.

n = 17  # целочисленный литерал
m = 7   # целочисленный литерал

# Целочисленный тип данных int используют не только потому, что он встречается в реальном мире, но и потому, что он естественным образом возникает при создании большинства программ.


# # ---------------------------------------------------------------
# # Преобразование строки в целое число
# # ---------------------------------------------------------------

# Для преобразования строки в целое число, мы используем команду int():

num = int(input())  # преобразование считанной строки в целое число

# Для преобразования строки в целое число не обязательно использовать команду input().

# Следующий код преобразует строку 12345 в целое число:

n = int('12345')  # преобразование строки в целое число

# Если строка не является числом, то при преобразовании возникнет ошибка.


# # ---------------------------------------------------------------
# # Целочисленные операторы
# # ---------------------------------------------------------------

# Язык Python предоставляет четыре основных арифметических оператора для работы с целыми числами (+, −, *, /), а также три дополнительных (% для остатка, // для целочисленного деления и ** для возведения в степень).

# Следующая программа демонстрирует все целочисленные операторы:


a = 13
b = 7

total = a + b
diff = a - b
prod = a * b
div1 = a / b
div2 = a // b
mod = a % b
exp = a ** b

print(a, '+', b, '=', total)
print(a, '-', b, '=', diff)
print(a, '*', b, '=', prod)
print(a, '/', b, '=', div1)
print(a, '//', b, '=', div2)
print(a, '%', b, '=', mod)
print(a, '**', b, '=', exp)


# # ---------------------------------------------------------------
# # Длинная арифметика
# # ---------------------------------------------------------------

# Отличительной особенностью языка Python является неограниченность целочисленного типа данных. По факту, размер числа зависит только от наличия свободной памяти на компьютере. Это отличает Python от таких языков как C++, C, C#, Java где переменные целого типа данных имеют ограничение. Например, в языке C# диапазон целых чисел ограничен от − 2 63 −2 63 до 2 63 − 1 2 63 −1.

atom = 10 ** 80  # количество атомов во вселенной
print('Количество атомов =', atom)

# Результатом выполнения программы будет число с 81 цифрой:

# Количество атомов = 100000000000000000000000000000000000000000000000000000000000000000000000000000000


# # ---------------------------------------------------------------
# # Символ разделитель
# # ---------------------------------------------------------------

# Для удобного чтения чисел можно использовать символ подчеркивания:

num1 = 25_000_000
num2 = 25000000
print(num1)
print(num2)

# Результатом выполнения такого кода будет:

25000000
25000000


# # ---------------------------------------------------------------
# # Числа с плавающей точкой
# # ---------------------------------------------------------------

# Наравне с целыми числами в Python есть возможность работы с дробными (вещественными) числами. Так, например, числа 2 3 , 2 , π 3 2 ​ , 2 ​ ,π – являются вещественными и целого типа int недостаточно для их представления.

# Дробные (вещественные) числа в информатике называют числами с плавающей точкой.

# Для представления чисел с плавающей точкой в Python используется тип данных float.

e = 2.71828  # литерал с плавающей точкой
pi = 3.1415  # литерал с плавающей точкой
# В Python, когда вы используете операцию деления /, результат всегда будет числом с плавающей точкой, даже если оба числа являются целыми. Вот пример:

print(4 / 2)  # Результат: 2.0, а не 2
# В отличие от математики, где разделителем является запятая, в информатике используется точка при записи чисел с плавающей точкой.


# # ---------------------------------------------------------------
# # Преобразование строки к числу с плавающей точкой
# # ---------------------------------------------------------------

# Для преобразования строки к числу с плавающей точкой мы используем команду float():

num = float(input()) # преобразование считанной строки в число с плавающей точкой
# Для преобразования строки к числу с плавающей точкой необязательно использовать команду input().

# Следующий код преобразует строку 1.2345 к числу с плавающей точкой:

n = float('1.2345')  # преобразование строки к числу с плавающей точкой
# Если строка не является числом, то при преобразовании возникнет ошибка.


# # ---------------------------------------------------------------
# # Арифметические операторы
# # ---------------------------------------------------------------

# Язык Python предоставляет четыре основных арифметических оператора для работы с числами с плавающей точкой (+, −, *, /) и один дополнительный (** – для возведения в степень).

# Следующая программа демонстрирует арифметические операторы:

a = 13.5
b = 2.0

total = a + b
diff = a - b
prod = a * b
div = a / b
exp = a ** b

print(a, '+', b, '=', total)
print(a, '-', b, '=', diff)
print(a, '*', b, '=', prod)
print(a, '/', b, '=', div)
print(a, '**', b, '=', exp)

# В результате работы такой программы будет выведено:

13.5 + 2.0 = 15.5
13.5 - 2.0 = 11.5
13.5 * 2.0 = 27.0
13.5 / 2.0 = 6.75
13.5 ** 2.0 = 182.25

# Деление на ноль приводит к ошибке.


# # ---------------------------------------------------------------
# # Преобразование между int и float
# # ---------------------------------------------------------------

# Неявное преобразование. Любое целое число (тип int) можно использовать там, где ожидается число с плавающей точкой (тип float), поскольку при необходимости Python автоматически преобразует целые числа в числа с плавающей точкой.

# Явное преобразование. Число с плавающей точкой нельзя неявно преобразовать в целое число. Для такого преобразования необходимо использовать явное преобразование с помощью команды int().

num1 = 17.89
num2 = -13.56
num3 = int(num1)
num4 = int(num2)
print(num3)
print(num4)

# Результатом выполнения такого кода будет:

17
-13

# Обратите внимание, что преобразование чисел с плавающей точкой в целое производится с округлением в сторону нуля, то есть int(1.7) = 1, int(-1.7) = -1.

# Не путайте операцию преобразования и округления. Для округления чисел с плавающей точкой используются дополнительные команды. О них расскажем позже.


# Начинающих программистов необходимость преобразования типов зачастую раздражает, но опытные знают, что внимание к типам данных — залог успеха и способ избежать ошибок. В 1996 году французская ракета взорвалась в воздухе из-за проблемы преобразования типов. Хотя ошибка в вашей программе может и не привести к взрыву, все равно имеет смысл уделить время изучению преобразования типов. Написав несколько программ, вы убедитесь, что понимание типов данных помогает не только писать компактный код, но и ясно излагать свои намерения, избегая ошибок в нюансах.


# # ---------------------------------------------------------------
# # Функции min() и max()
# # ---------------------------------------------------------------

# Для определения соответственно минимального или максимального значения используются функции min() и max(). Аргументов у этих функций может быть любое количество, главное, чтобы они все поддерживали между собой операцию сравнения (например, float и int поддерживают сравнение, а float и str - нет).

# Например, результатом выполнения следующего кода:

a = max(3, 8, -3, 12, 9) # 12
b = min(3, 8, -3, 12, 9) # -3
c = max(3.14, 2.17, 9.8) # 9.8


# # ---------------------------------------------------------------
# # Функция abs()
# # ---------------------------------------------------------------

# Для нахождения модуля (абсолютной величины) числа в Python используется функция abs().

# Модулем (абсолютной величиной) положительного числа называется само число, модулем отрицательного числа называется противоположное ему число, модуль нуля – нуль. Модуль числа a a обозначается ∣ a ∣ ∣a∣, для него имеет место равенство:

# ∣a∣ =  ⎨ ​ a, 0, −a, ​ если a>0 если a=0 если a<0 ​

# Например, результатом выполнения следующего кода:

print(abs(10))      # 10
print(abs(-7))      # 7
print(abs(0))       # 0
print(abs(-17.67))  # 17.67