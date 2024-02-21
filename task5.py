import re


def find_dates(text):

    pattern = r'\b\d{1,2}\s(?:января|февраля|марта|апреля|мая|июня|июля|августа|сентября|октября|ноября|декабря)\s\d{4}\b'

    dates = re.findall(pattern, text)

    return dates


text = " 10 февраля 2004, 15 марта 2023, 12.03.2024 "
found_dates = find_dates(text)
print("Найденные даты:", found_dates)
