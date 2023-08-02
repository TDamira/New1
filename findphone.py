import re


def is_valid_phone_number(number):
    pattern = r'^\+996 \(\d{3}\) \d{3}-\d{3}$'
    return bool(re.match(pattern, number))

phone_number = "+996 (555) 000-929"
print(is_valid_phone_number(phone_number))
