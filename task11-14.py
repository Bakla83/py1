# 2
def calculate_average_ascii_weight(string):
    if not string:
        return 0
    return sum(ord(char) for char in string) / len(string)

def sort_strings_by_average_ascii_weight(strings):
    return sorted(strings, key=calculate_average_ascii_weight)
# 4
def calculate_standard_deviation_difference(string, reference_string):
    if not string:
        return 0
    avg_weight = calculate_average_ascii_weight(string)
    reference_avg_weight = calculate_average_ascii_weight(reference_string)
    return (avg_weight - reference_avg_weight) ** 2

def sort_strings_by_standard_deviation_difference(strings, reference_string):
    return sorted(strings, key=lambda x: calculate_standard_deviation_difference(x, reference_string))
# 7
def count_vowel_consonant_combinations(string):
    vowels = "aeiouAEIOU"
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    vowel_consonant_count = 0
    consonant_vowel_count = 0
    for i in range(len(string) - 1):
        if string[i] in vowels and string[i + 1] in consonants:
            vowel_consonant_count += 1
        elif string[i] in consonants and string[i + 1] in vowels:
            consonant_vowel_count += 1
    return abs(vowel_consonant_count - consonant_vowel_count)

def sort_strings_by_vowel_consonant_combinations_difference(strings):
    return sorted(strings, key=count_vowel_consonant_combinations)

# 11
def calculate_max_ascii_trio_variance(string):
    max_trio_variance = 0
    for i in range(len(string) - 2):
        trio_weight = (ord(string[i]) + ord(string[i + 1]) + ord(string[i + 2])) / 3
        trio_variance = ((ord(string[i]) - trio_weight) ** 2 + (ord(string[i + 1]) - trio_weight) ** 2 + (ord(string[i + 2]) - trio_weight) ** 2) / 3
        max_trio_variance = max(max_trio_variance, trio_variance)
    return max_trio_variance

def sort_strings_by_max_ascii_trio_variance(strings, reference_string):
    return sorted(strings, key=lambda x: calculate_max_ascii_trio_variance(x) - calculate_max_ascii_trio_variance(reference_string))

print("Выберите одну из задач:")
print("2. В порядке увеличения среднего веса ASCII-кода символов строки.")
print("4. В порядке увеличения квадратичного отклонения среднего веса ASCII-кода символов строки от среднего веса ASCII-кода символов первой строки.")
print("7. В порядке увеличения разницы между количеством сочетаний 'гласная-согласная' и 'согласная-гласная' в строке.")
print("11. В порядке квадратичного отклонения дисперсии максимального среднего веса ASCII-кода троек символов в строке от максимального среднего веса ASCII-кода троек символов в первой строке.")

choice = input("Введите номер задачи (2, 4, 7 или 11): ")

if choice == '2':
    strings = input("Введите строки через запятую: ").split(',')
    result = sort_strings_by_average_ascii_weight(strings)
elif choice == '4':
    strings = input("Введите строки через запятую: ").split(',')
    reference_string = strings[0] if strings else ''
    result = sort_strings_by_standard_deviation_difference(strings, reference_string)
elif choice == '7':
    strings = input("Введите строки через запятую: ").split(',')
    result = sort_strings_by_vowel_consonant_combinations_difference(strings)
elif choice == '11':
    strings = input("Введите строки через запятую: ").split(',')
    reference_string = strings[0] if strings else ''
    result = sort_strings_by_max_ascii_trio_variance(strings, reference_string)




