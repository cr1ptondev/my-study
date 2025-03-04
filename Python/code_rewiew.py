# ---------------------------------------------------------------
# Обучение на Python курс "Поколение Python": курс для начинающих
# ---------------------------------------------------------------


# ---------------------------------------------------------------
# Тема урока: ревью кода
# ---------------------------------------------------------------

# ---------------------------------------------------------------
# Ревью кода
# ---------------------------------------------------------------

# Ревью кода – проверка исходного кода программы с целью обнаружения и исправления ошибок и неточностей, которые остались незамеченными при начальной разработке. 

# В процессе ревью кода могут быть исправлены:

# фактические ошибки;
# производительность кода;
# читабельность кода и ошибки форматирования кода.

# Целью ревью кода является улучшение качества программного кода и совершенствование навыков программиста.
# Как правило, ревью кода выполняет программист с большим опытом.

# ---------------------------------------------------------------
# Фактические ошибки
# ---------------------------------------------------------------

# К фактическим ошибкам в коде относятся ошибки, из-за которых код может работать неверно. По сути, это ошибки, относящиеся к алгоритму, который используется в программе для решения задачи.

# Среди частых фактических ошибок встречаются:

# отсутствие начальной инициализации переменной;
# неправильная начальная инициализация переменной;
# отсутствие отступа (в Python блоки кода выделяются отступами);
# неправильные числовые граничные значения, например при использовании функции range();
# неправильные граничные сравнения (путаница с >, >= или <, <=);
# путаница логических операций or и and и т.д.

# ---------------------------------------------------------------
# Производительность кода
# ---------------------------------------------------------------

# Под производительностью кода в простейшем случае можно подразумевать то, сколько времени программа тратит на решение задачи. При написании программы, программист должен думать над тем, сколько времени в худшем случае потребуется его программе для решения задачи.

# Рассмотрим задачу, которая проверяет число на простоту.

# 1 версия программы: Перебираем все числа от 2 до num - 1 (включительно) и делаем проверку делимости числа num на i:

num = int(input())
flag = True

for i in range(2, num):
    if num % i == 0:
        flag = False

if num > 1 and flag == True:
    print('Число простое')
else:
    print('Число составное')

# Если программе на вход подаётся простое число num = 1934234249, то она будет работать примерно 270 секунд = 4.5 минуты. 


# 2 версия программы: Несложно понять, что перебирать все числа от 2 до num - 1 (включительно) не имеет смысла. Достаточно проверить числа от 2 до num // 2 (включительно):

num = int(input())
flag = True

for i in range(2, num // 2 + 1):
    if num % i == 0:
        flag = False

if num > 1 and flag == True:
    print('Число простое')
else:
    print('Число составное')

# Если программе на вход подается простое число num = 1934234249, то она будет работать примерно 130 секунд = 2.2 минуты. По сути мы улучшили время работы программы вдвое! 

# 3 версия программы: Правую границу num // 2 проверки можно улучшить, если заметить, что у любого составного числа есть делитель (отличный от 1 1), не превосходящий квадратного корня из числа. Таким образом, имеет смысл перебирать делители от 2 2 до n u m num ​ (включительно).

num = int(input())
flag = True

for i in range(2, int(num ** 0.5) + 1):
    if num % i == 0:
        flag = False

if num > 1 and flag == True:
    print('Число простое')
else:
    print('Число составное')

# Если программе на вход подаётся простое число num = 1934234249, то она будет работать примерно 0.066 секунд. По сути мы улучшили время работы программы в 4000 раз! 😎

# 4 версия программы: Предыдущие оптимизации касались случая, когда проверяемое число является простым. В случае если число является составным и мы нашли его первый делитель (отличный от 1), мы прерываем цикл с помощью оператора break:

num = int(input())
flag = True

for i in range(2, int(num ** 0.5) + 1):
    if num % i == 0:
        flag = False
        break

if num > 1 and flag == True:
    print('Число простое')
else:
    print('Число составное')

# ---------------------------------------------------------------
# Читабельность кода
# ---------------------------------------------------------------

# Следует помнить, что наш код должен легко читаться другими программистами. Чтобы этого достичь, следует придерживаться стандарта PEP 8. Обращайте внимание на следующие моменты:

# отступы и пробелы: используйте 4 пробела на один уровень отступа и никогда не смешивайте символы табуляции и пробелы;
# названия переменных: используйте говорящие названия для переменных (total, counter, product) и следуйте стилю lower_case_with_underscores (слова из маленьких букв с подчеркиваниями);
# пустые строки: дополнительные отступы пустыми строками могут быть изредка полезны для выделения группы логически связанных частей программы: инициализация переменных, основной алгоритм, завершающая проверка и т.д.;
# комментарии: комментарии должны являться законченными предложениями. И помните, комментарии, которые противоречат коду, хуже, чем отсутствие комментариев. Всегда исправляйте комментарии, если меняете код!
#    О стандарте PEP 8 на русском языке можно почитать https://pythonworld.ru/osnovy/pep-8-rukovodstvo-po-napisaniyu-koda-na-python.html

# ---------------------------------------------------------------
# Примечания
# ---------------------------------------------------------------

# Примечание 1. Хорошие статьи о ревью кода можно почитать на хабре: https://habr.com/ru/post/340550/ , https://habr.com/ru/post/342244/

# Примечание 2. Программные ошибки, часто называют багами 🦟

# Примечание 3. Все программисты создают баги, особенно в начале своего карьерного пути. Это норма 

# ---------------------------------------------------------------
# Примеры
# ---------------------------------------------------------------

# Пример 1. Требовалось написать программу, которая выводит 10 раз символ А. Вы ревьювите приведённый ниже код:

print('A')
print('A')
print('A')
print('A')
print('A')
print('A')
print('A')
print('A')
print('A')
print('A')

# Что вы о нём скажете? Правильно ли он работает? Как его улучшить?

# Ревью. Приведённый выше код выполняет поставленную задачу, однако его можно улучшить. Поскольку действия в строках одинаковые, то можно использовать цикл. Поскольку мы знаем количество повторений (итераций), то нам подходит цикл for:

for _ in range(10):
    print('A')


# Пример 2. Требовалось написать программу, которая должна вывести все числа от 1 до 100, кратные 7. Вы ревьювите приведённый ниже код:

i = 1
while i < 101:
    if i % 7 == 0:
        print(i)
        i += 1

# Что вы о нём скажете? Правильно ли он работает? Как его улучшить?

# Ревью. Приведённый выше код содержит достаточно распространённую ошибку: неверно поставленный отступ. Поскольку управление циклом while происходит при помощи переменной i, то её необходимо инкрементировать (увеличивать) каждую итерацию. В приведённом выше коде она инкрементируется, только если выполняется условие i % 7 == 0, которое ложно для начального значения i = 1. Таким образом, получаем бесконечный цикл. Для исправления ошибки необходимо удалить отступ у строки i += 1:

i = 1
while i < 101:
    if i % 7 == 0:
        print(i)
    i += 1
# В данном случае лучше использовать цикл for с шагом, равным 7. Это позволит сделать код более наглядным и сократит время выполнения программы, так как нет необходимости просматривать и проверять все числа на делимость на 7:

for i in range(7, 101, 7):
    print(i)


# Пример 3. Требовалось написать программу, которая выводит все числа от 100 до 1 в порядке убывания. Вы ревьювите приведённый ниже код:

for i in range(1, 100):
    print(101 - i)

# Что вы о нём скажете? Правильно ли он работает? Как его улучшить?

# Ревью. Приведенный код содержит достаточно распространенную ошибку: неправильная правая граница цикла for. Следует помнить, что правая граница в цикле for всегда не включительна. Таким образом, для исправления ошибки необходимо заменить число 100 на 101:

for i in range(1, 101):
    print(101 - i)

# В данном случае лучше использовать цикл for с шагом, равным −1:

for i in range(100, 0, -1):
    print(i)


# Пример 4. Требовалось написать программу, которая находит сумму всех нечётных чисел от 1 до 1000 (включительно). Вы ревьювите приведённый ниже код:

a = 1
for i in range(1, 1000):
    if i % 2 == 1:
        a = a + 1
print(a)

# Что вы о нем скажете? Правильно ли он работает? Как его улучшить?

# Ревью. Приведенный код содержит достаточно распространенные ошибки:

# неправильная начальная инициализация переменной a; 
# неправильная правая граница цикла for;
# неправильно записанная операция накапливания значения суммы.

a = 0
for i in range(1, 1001):
    if i % 2 == 1:
        a = a + i
print(a)

# Для улучшения читабельности кода изменим название переменной a на total и используем расширенный оператор присваивания:

total = 0
for i in range(1, 1001, 2):
    total += i
print(total)


# Пример 5. Требовалось написать программу, которая вычисляет факториал числа. Вы ревьювите следующий код:

n = input()
a = 0
for i in range(n):
    a = a * i
print(a)

# Что вы о нем скажете? Правильно ли он работает? Как его улучшить?

# Ревью. Приведенный код содержит достаточно распространенные ошибки:
# отсутствие преобразования строки текста в целое число;
# неправильная начальная инициализация переменной a; 
# неправильная работа с границами итерирования: переменная i принимает значения от 0 до n - 1.

n = int(input())
a = 1
for i in range(1, n + 1):
    a = a * i
print(a)

# Для улучшения читабельности кода, изменим название переменной a на factorial и используем расширенный оператор присваивания:

n = int(input())
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print(factorial)

# В модуле math есть функция factorial(), которая вычисляет факториал числа. Поэтому вместо реализации своей версии куда правильнее и удобнее воспользоваться уже готовой.



# На обработку поступает последовательность из 10 целых чисел (каждое на отдельной строке). Известно, что вводимые числа по абсолютной величине не превышают 10 ** 6 . Нужно написать программу, которая выводит на экран сумму всех отрицательных чисел последовательности и максимальное отрицательное число в последовательности. Если отрицательных чисел нет, требуется вывести на экран «NO» (без кавычек). Программист торопился и написал программу неправильно.

# Найдите все ошибки в этой программе (их ровно 5). Известно, что каждая ошибка затрагивает только одну строку и может быть исправлена без изменения других строк.