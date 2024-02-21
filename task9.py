def sort_strings_by_length():
    strings = []
    while True:
        string = input("Введите строку: ")
        if not string:
            break
        strings.append(string)
    return sorted(strings, key=len)

sorted_strings = sort_strings_by_length()

print("Упорядоченный список строк:")
for string in sorted_strings:
    print(string)
