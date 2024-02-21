'''def sort_checker(text):
    sorted_text = ''.join(sorted(text))
    return sorted_text == text


print(sort_checker('acbaa'))'''


def count_letter_A(s):
    return s.count("A")


string = "AbAcAda"
print("Количество букв 'A' в строке:", count_letter_A(string))
