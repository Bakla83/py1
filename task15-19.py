def find_min_index(arr):
    if not arr:
        return -1
    min_index = arr.index(min(arr))
    return min_index

def count_elements_in_range(arr, a, b):
    count = sum(1 for x in arr if a <= x <= b)
    return count

def count_elements_between_min(arr):
    if not arr:
        return 0
    min_index_first = arr.index(min(arr))
    min_index_last = len(arr) - 1 - arr[::-1].index(min(arr))
    count = abs(min_index_last - min_index_first) - 1
    return count

def count_elements_in_segment(arr, a, b):
    count = sum(1 for x in arr if a <= x <= b)
    return count

def unique_elements_in_one_list(L1, L2):
    unique_L1 = [x for x in L1 if x not in L2]
    unique_L2 = [x for x in L2 if x not in L1]
    return unique_L1 + unique_L2

print("Выберите одну из задач:")
print("2. Найти индекс минимального элемента в массиве.")
print("14. Найти количество элементов в заданном интервале.")
print("26. Найти количество элементов между первым и последним минимальным в массиве.")
print("38. Найти количество элементов, значение которых принадлежит заданному отрезку.")
print("50. Построить новый список из элементов, встречающихся только в одном из двух списков и не повторяющихся.")

choice = input("Введите номер задачи (2, 14, 26, 38, 50): ")

result = None

if choice == '2':
    array = [int(x) for x in input("Введите элементы массива через пробел: ").split()]
    result = find_min_index(array)
elif choice == '14':
    array = [int(x) for x in input("Введите элементы массива через пробел: ").split()]
    a, b = map(int, input("Введите интервал a..b: ").split())
    result = count_elements_in_range(array, a, b)
elif choice == '26':
    array = [int(x) for x in input("Введите элементы массива через пробел: ").split()]
    result = count_elements_between_min(array)
elif choice == '38':
    array = [int(x) for x in input("Введите элементы массива через пробел: ").split()]
    a, b = map(int, input("Введите отрезок a..b: ").split())
    result = count_elements_in_segment(array, a, b)
elif choice == '50':
    L1 = [int(x) for x in input("Введите элементы первого списка через пробел: ").split()]
    L2 = [int(x) for x in input("Введите элементы второго списка через пробел: ").split()]
    result = unique_elements_in_one_list(L1, L2)

if result is not None:
    print("Результат:", result)

