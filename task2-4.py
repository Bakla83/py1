def sort_checker(text):
    sorted_text = ''.join(sorted(text))
    return sorted_text == text

print(sort_checker('acbaa'))

