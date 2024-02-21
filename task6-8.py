def find_lowercase_latin_characters(text):
    lowercase_latin_chars = set()
    for char in text:
        if char.islower() and char.isalpha():
            lowercase_latin_chars.add(char)
    return lowercase_latin_chars


def count_unique_latin_characters(text):
    unique_latin_chars = set()
    for char in text:
        if char.isalpha():
            unique_latin_chars.add(char.lower())
    return len(unique_latin_chars)


def find_file_name_without_extension(file_path):
    base_name = file_path.split('/')[-1]
    if '.' in base_name:
        return base_name.rsplit('.', 1)[0]
    return base_name


print("Выберите одну из задач:")
print("1. Найти все строчные символы латиницы, которые используются в строке.")
print("2. Найти количество задействованных символов латиницы в строке (без дубликатов).")
print("3. Найти имя файла без расширения в строке, которая представляет путь к файлу.")
choice = input("Введите номер задачи (1, 2 или 3): ")

if choice == '1':
    text = input("Введите строку: ")
    result = find_lowercase_latin_characters(text)
    print("Строчные символы латиницы, используемые в строке:", result)
elif choice == '2':
    text = input("Введите строку: ")
    result = count_unique_latin_characters(text)
    print("Количество задействованных символов латиницы в строке:", result)
elif choice == '3':
    file_path = input("Введите путь к файлу: ")
    result = find_file_name_without_extension(file_path)
    print("Имя файла без расширения:", result)
else:
    print("Некорректный ввод. Пожалуйста, выберите число от 1 до 3.")
