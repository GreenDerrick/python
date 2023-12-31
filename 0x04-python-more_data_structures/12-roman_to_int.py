#!/usr/bin/python3
def roman_to_int(roman_string):
    dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 100}
    result = 0
    if not roman_string or roman_string == "":
        return 0
    
    if len(roman_string) >= 2:
        if dic[roman_string[0]] < dic[roman_string[1]]:
            for i in roman_string[1::]:
                result += dic[i]
            res -= dic[roman_string[0]]
            return result

    for i in roman_string:
        result += dic[i]
    return result
