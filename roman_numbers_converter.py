import roman
import re


def convert(number):
    if number.group().__len__() > 0:
        return str(roman.fromRoman(number.group()))
    else:
        return number.group()


file = open('resources/input.txt', 'r', encoding='utf-8')
source = file.read()
file.close()

regexp = r"(?:M*(?:LD|LM|CM|CD|D?C{0,3})(?:VL|VC|XC|XL|L?X{0,3})(?:IX|IV|V?I{0,3}))"
pattern = re.compile(regexp, re.UNICODE)

result = re.sub(pattern, convert, source)

file = open('resources/output.txt', 'w', encoding='utf-8')
file.write(result)
file.close()
