#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    result_int = 0
    roman_number = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for i in range(len(roman_string)):
        current_number = roman_number[roman_string[i]]
        if i + 1 < len(roman_string):
            next_number = roman_number[roman_string[i+1]]
            if current_number < next_number:
                result_int -= current_number
            else:
                result_int += current_number
    else:
        decimal_number += current_number
    return result_int
