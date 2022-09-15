def salary():
    sal=int(input('Enter salary\n'))
    return sal

def da(a):
    print("DA:",(0.4)*a+a)

def hra(a):
    print("HRA:",(0.2*a)+a)

def bonus(a):
    a=a+(0.1*a)
    print("Bonus:",a)