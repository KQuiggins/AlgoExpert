s = "LVIII"
def roman_to_int(s):
    roman_to_int_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    result = 0
    prev_value = 0
    for c in s:
        current_value = roman_to_int_dict[c]
        if current_value > prev_value:
            result -= 2 * prev_value
        result += current_value
        prev_value = current_value
    return result

print(roman_to_int(s))