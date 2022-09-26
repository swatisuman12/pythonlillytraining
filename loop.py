#for loop
'''
m = str(input('enter name:'))
for name in m:
    print(name)
course = ['c','c++','python','java','html']
for item in course:
    print(item)
num = (1,2,3,4,5)
sum = 0
for i in num:
    sum= sum + i
    print(sum)
print(f'the sum is {sum}')
#nested loop
course = ['c','c++','python','java','html']
for courses in course:   
    print(f'subjects are {courses}')
    for units in courses:   # in nested loop, the inner loop dont have reference of outer variables. we should consider word taken with for loop
        print(f'units are {units}')
a = input('enter name: ')
for name in {a}:
    if len(name)<1:
        print('enter name')
    if name.isalpha()== False:
        print(f'its compulsory to enter name with alphabets only {name} is invalid')
    else:
        print(name)
b = input('enter number: ')
for phone in {b}:
    if len(phone)==10 or phone.isnumeric()==True:
        print(f'{phone}')
    else:
        print('invalid')
c = int(input('age: ')) 
if c<18:
    print('age should be greater than 18')
else:
    print(c)
d = input('email: ')
if len(d)<=10:
    print('invalid')
else:
    print(d)
e = input('address: ')
print(e)
for x in range(3):
    print(x)
for y in range(1,20,5):
    print(y)
#while loop
#break continue
i = 0
while(True):
    print(i)
    if i ==4:
        break
    i=i+1 
num = [1,-1,2,-2,3,-3]
psum = 0
for nums in num:
    if nums<0:
        continue
    psum += nums
print(f'sum is {psum}')
'''