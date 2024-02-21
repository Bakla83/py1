# 2
'''def sort_checker(text):
    sorted_text = ''.join(sorted(text))
    return sorted_text == text


print(sort_checker('acbaa'))'''


# 10
'''def count_letter_A(s):
    return s.count("A")


string = "AbAcAda"
print("Количество букв 'A' в строке:", count_letter_A(string))'''

# 17
import os


def find_file_name(file_path):
    base_name = os.path.basename(file_path)
    file_name = os.path.splitext(base_name)[0]
    return file_name


file_path = r"C:\Users\263\Desktop\курс 2.2\phyton\Text doc.txt"
file_name = find_file_name(file_path)
print("Имя файла:", file_name)





