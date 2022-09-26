
import re

text =("monika 444")

pattern = re.compile(r'\d\d')
matches = pattern.search(text)
print(matches)


text1 =('today is 15-sep-2022 and its engineers day. 16.aug-2022, 17/08/22,18-aug-2022')   
pattern=re.compile(r'\d{2}[\./-]([a-zA-Z]{3}|\d{2})[-\./]\d{2,4}')
matches = pattern.finditer(text1)
for match in matches:
    print(match.group())

text2 = ('monika@gmail.com support@lilly.co.in monika@outlook.com')
pattern = re.compile(r'\w+@[a-z]+(\.[a-z]{2,3})+') # + is used if more values needed to print
matches = pattern.finditer(text2)
for match in matches:
    print(match.group())

text3 = ('123-456 789, 098-76543-210,123-4567890, +6099.100')
pattern = re.compile(r'(\+\d)?\d{3}[.-]\d{3}\s?\d{4}')
matches = pattern.finditer(text3)
for match in matches:
    print(match.group())