# a line is a part of code and there is an error, if its not much imp, use try, except
print('enter first number: ')
a = input()
print('enter second number: ')
b = input()
try:
    print('the addition is:',int(a)+int(b))
except Exception as y:
    print(y)
print('yes')