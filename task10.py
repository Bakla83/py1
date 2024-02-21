def sort_strings_by_word_count():
    strings = []
    while True:
        string = input("Введите строку: ")
        if not string:
            break
        strings.append(string)
    return sorted(strings, key=lambda x: len(x.split()))

sorted_strings = sort_strings_by_word_count()

print("Упорядоченный список строк по количеству слов:")
for string in sorted_strings:
    print(string)
