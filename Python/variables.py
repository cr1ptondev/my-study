# # ---------------------------------------------------------------
# # Обучение на Python курс "Поколение Python": курс для начинающих
# # ---------------------------------------------------------------


# # -----------------------------
# # Тема урока: Variables - переменные
# # -----------------------------

# # Записываем в переменную с именем variable_name данные введенные с клавиатуры и выводим указания переменной в аргументе функции print на экран

# # variable_name = input()
# # print('Вы ввели текст:', variable_name)

# # Присваиваем значение переменной city ( city - имя,а 'New York' - значение)

# city = 'New York'
# print(city, '- город в Америке')

# # Мы можем использовать несколько переменных в команде print(), нам это никто не запрещает. Только стоит помнить, что аргументы в команде print() нужно отделять запятыми друг от друга.

# name = 'Vadim'
# country = 'Russia'
# print('Имя:', name,'.', 'Страна:', country)

# # В имени переменной рекомендуется использовать только латинские буквы a-z, A-Z, цифры и символ нижнего подчеркивания (_) , Имя переменной не может начинаться с цифры , Имя переменной не может содержать пробелы , Имя переменной по возможности должно отражать ее назначение

# # Python – регистрочувствительный язык. Переменные name и Name – две совершенно разные переменные. 

# # Для именования переменных принято использовать стиль lower_case_with_underscores (слова из маленьких букв с подчеркиваниями). Например, следующие имена для переменных хорошие:

# server_response = 12312
# is_password_good = '324211'
# username = 'Robot'
# cyberpunk_77 = '1eProton9'

# # Значение переменной — это сохранённая в ней информация: текст, число и т.д.

# # Символ = в языках программирования выступает в роли оператора присваивания. Он выполняет задачу связывания значения, расположенного справа от него, с именем переменной, указанной слева. Таким образом, переменная слева "принимает" или "хранит" значение, представленное выражением справа от знака =

# print('Как тебя зовут?')

# name = input()
# print('Привет,', name)

# name = 'Timur'
# print('Привет,', name)

# # Оператор присваивания сообщает переменной то или иное значение независимо от того, была ли эта переменная введена раньше. Вы можете менять значение переменной, записав еще один оператор присваивания. Если у нас имеется переменная, мы можем делать с ней все что угодно — например, присвоить другой переменной или изменить значение.

# name1 = 'Джон'
# name2 = name1
# name1 = 'Гвидо'

# print(name1)
# print(name2)