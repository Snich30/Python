 # создание строки учебного заведения
college = "Московский государсвтенный колледж связи №54"

# просмотр доступных методов для строки
print(dir(college))

# просмотр документации для метода lower()
help(college.lower)

# создание строки country
country = 'usa'

# преобразование к верхнему регистру
correct_country = country.upper()

# создание строки filename
filename = 'hello.py'

# проверка суффикса файла
if filename.endswith('.java'):
    print("Файл является Java файлом")
else:
    print("Файл не является Java файлом")

# определение индекса подстроки 'py'
index_py = filename.find('py')
print("Индекс подстроки 'py':", index_py)

# проверка начала строки с подстроки 'world'
if filename.startswith('world'):
    print("Строка начинается с 'world'")
else:
    print("Строка не начинается с 'world'")

# просмотр раздела STRINGMETHODS
help(str.stringmethods)