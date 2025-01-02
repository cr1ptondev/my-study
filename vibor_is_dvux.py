# # ---------------------------------------------------------------
# # Обучение на Python курс "Поколение Python": курс для начинающих
# # ---------------------------------------------------------------


# # -----------------------------
# # Условный оператор if-else
# # -----------------------------

# # В Python существует несколько способов проверки, и в каждом случае возможны два исхода: истина (True) или ложь (False).

# # Проверка условий и принятие решений по результатам этой проверки называется ветвлением (branching). Программа таким способом выбирает, по какой из возможных ветвей ей двигаться дальше.

# # В Python проверка условия осуществляется при помощи ключевого слова if.

# # Двоеточие (:) в конце строки с инструкцией if сообщает интерпретатору Python, что дальше находится блок команд. В блок команд входят все строки с отступом под строкой с инструкцией if, вплоть до следующей строки без отступа.

# # Если условие истинно, выполняется весь расположенный ниже блок. В предыдущем примере блок инструкций составляет третья и четвертая строки программы.

# # Блоком кода называют объединенные друг с другом строки. Они всегда связаны с определенной частью программы (например, с инструкцией if). В Python блоки кода формируются при помощи отступов.

# # # Для того чтобы обеспечить возможность выполнять что-либо в случае, если условие оказалось ложным, мы используем ключевое слово else.

# print('Какой язык программирования мы изучаем?')
# answer = input()
# if answer == 'Python':
#     print('Верно! Мы ботаем Python =)')
#     print('Python - отличный язык!')
# else:
#     print('Не совсем так!')

# # В некоторых языках программирования отступы — дело личного вкуса, и можно вообще обходиться без них. Однако в Python они – неотъемлемая часть кода. Именно отступ сообщает интерпретатору Python, где начинается и где заканчивается блок кода.

# # Отступ — небольшое смещение строки кода вправо. В начале такой строки находятся пробелы, и поэтому она на несколько символов отстоит от левого края.

# # Некоторым инструкциям в Python (например, инструкции if) именно блок кода сообщает, какие действия следует предпринять. После if блок кода информирует интерпретатор Python, как действовать, если условие истинно, и как — если оно ложно.

# # По соглашению PEP 8, для отступа блоков кода используются 4 пробела. Если в среде VS Code или Wing IDE нажать на клавишу Enter после if, она автоматически выставит 4 пробела.


# # -----------------------------
# # Операторы сравнения
# # -----------------------------

# # Можно заметить, что в проверке условия мы использовали двойное равенство (==), вместо ожидаемого одиночного (=). Не стоит путать оператор присваивания (=) с условным оператором (==).

# # Оператор присваивания (=) присваивает переменным значения:


# # Для проверки двух элементов на равенство Python использует удвоенный знак равно (==). Вот так:

# # if answer == 'Python':
# #     ...

# # if name == 'Gvido':
# #     ...

# # if temperature == 40:
# #     ...

# # Путаница с операторами == и = является одной из самых распространенных ошибок в программировании. Эти символы используются не только в Python, и каждый день множество программистов используют их неправильно.

# # В Python существует 6 основных операторов сравнения.

# # x > 7, x < 7, x >= 7, x<= 7, x == 7, x != 7 (не равен)

# num1 = int(input())
# num2 = int(input())

# if num1 < num2:
#     print(num1, 'меньше чем', num2)
# if num1 > num2:
#     print(num1, 'больше чем', num2)

# if num1 == num2:  # используем двойное равенство
#     print(num1, 'равно', num2)
# if num1 != num2:
#     print(num1, 'не равно', num2)


# # -----------------------------
# # Цепочки сравнений
# # -----------------------------

# # Операторы сравнения в Python можно объединять в цепочки (в отличие от большинства других языков программирования, где для этого нужно использовать логические связки), например, a == b == c или 1 <= x <= 10. Следующий код проверяет, находится ли значение переменной age в диапазоне от 3 до 6:

# age = int(input())
# if 3 <= age <= 6:
#     print('Вы ребёнок')


# # Код, проверяющий равенство трех переменных, может выглядеть так:

# a = 3
# b = 4
# c = 4
# if a == b == c:
#     print('числа равны')
# else:
#     print('числа не равны')


# # -----------------------------
# # Транзитивность
# # -----------------------------

# # Операция равенства является транзитивной. Это означает, что если a == b и b == c, то из этого следует, что a == c. Именно поэтому предыдущий код, проверяющий равенство трех переменных, работает, как полагается. 

# # Из курса математики вам могут быть знакомы другие примеры транзитивных операций: 
# # Отношение порядка: если a > b и b > c, то a > c; 
# # Параллельность прямых: если a ∥ b и b ∥ c , то a ∥ c ; 
# # Делимость: если a делится на b и bделится на c, то a делится на c. 

# # Наглядно транзитивность отношения порядка можно понять на таком примере: если сосед слева старше вас ( a > b ) (a>b), а вы старше соседа справа ( b > c ) (b>c), то сосед слева точно старше соседа справа ( a > c ) (a>c). Операция неравенства (!=), в отличие от операции равенства (==), является нетранзитивной. То есть из того, что a != b и b != c вовсе не следует, что a != c. Действительно, если вас зовут не так, как соседа слева и не так, как соседа справа, то нет гарантии, что у обоих соседей не окажутся одинаковые имена.

# if a != b != c:
#     print('числа не равны')
# else:
#     print('числа равны')


# # Задача 1. Напишите программу, которая считывает одну строку. Если это строка «Python», программа выводит «ДА», в противном случае программа выводит «НЕТ».

# word = input()

# if word == 'Python':
#     print('ДА')
# else:
#     print('НЕТ')

# # Задача 2. Напишите программу, которая определяет, состоит ли двузначное число, введенное с клавиатуры, из одинаковых цифр. Если состоит, то программа выводит «ДА», в противном случае программа выводит «НЕТ».

# num = int(input())

# last_digit = num % 10    # последняя цифра числа
# first_digit = num // 10  # первая цифра числа

# if last_digit == first_digit:
#     print('ДА')
# else:
#     print('НЕТ')

# # Задача 3. Напишите программу, которая считывает три числа и подсчитывает количество чётных чисел.

# num1, num2, num3 = int(input()), int(input()), int(input())

# counter = 0  # переменная счётчик
# if num1 % 2 == 0:
#     counter = counter + 1  # увеличиваем счётчик на 1
# if num2 % 2 == 0:
#     counter = counter + 1  # увеличиваем счётчик на 1
# if num3 % 2 == 0:
#     counter = counter + 1  # увеличиваем счётчик на 1

# print(counter)
