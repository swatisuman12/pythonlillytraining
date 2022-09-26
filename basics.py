'''
#print(' hello', end ='hi')
#print('bye')
print('swati','suman', sep = ',',end ='.')
print('sinha')
print('swati','sinha')

escape sequence

print('karnataka\"s')
print('hi:\"swati\"')
print('hello \t bengaluru')
print('hello \n bengaluru')
print("helloo\b bengaluru")


#hexadecimal
hexadecimal number: 48454C4C4F20574F524C44
print("\x48\x45\x4C\x4C\x4F\x20\x57\x4F\x52\x4C\x44")

igonre
print(r"hi\n hello\b")

#STORE THE OUTPUT INSIDE THE FILE
x=open("sample.txt",'w')
print("world",file = x)
x.close()
write cat sample.txt in terminal to execute it . it wont come directly
'''
# declare variables

a='swati'
b=44
b2=6
d = 'cr'
'''
print(a)
print(type(a))
print(type(b))
b3=b+b2
print(b3) = 50
concatination
c=a+b 
print(c)

c=a+b 
print(c)

a='swati'
print(a*2) = swatiswati

b= 10
print(b*2) = 20


#option 2 to combine the text with join method
print(''.join([a,d]))

#option 3: 
print("% s % s" % (a,d))
#option 4
print("{} {}".format(a,d))'''

#type casting

var1 = '10'
var2 ='20'
var3 = 'swati'

print(int(var1)+int(var2))
print('enter any positive number')
var4=input()
print(var4)



from datetime import date


print("enter your first name",end =" ")
a= input()
print("enter your last name")
b=input()
#print("name: " + a+b)
print("enter date of birth")
c = int(input())
today = date.today()
age=today.year - c #- ((today.month,today.day) < (c.month,c.day))
print("enter phone number")
d = int(input())
print("name: " + a+ ' '+b )
print("dob: " ,c)
print("age: " ,age)
print("phone: ", d)


#string slice
string = "introduction"
print(string[3])
print(string[0:5])
print(string[5:])
print(len(string))
print(string[:])
print(string[::])
print(string[::2]) # alternate letters, skips
print(string[::20]) #only first letter is printed since 20th character is not there
print(string[::-1])#reverse
print(string[::-2]) #reverse

print(string.isalnum()) #alphanumeric, if spacing is there then its not alpha numeric
print(string.isalpha()) #--||--
print(string.find("ion")) # gives index if that letter or word is there
print("int" in string) #tells truth or false if word is there or not
print(string.endswith("ion"))
print(string.count("i"))
print(string.replace("tion","ing")) # its only changes in print function. original string remains same
print(string.upper())
print(string.lower())
print(string.capitalize())


str = string[::-1]
for i in range(0,12):
    print(string[i])
    print(str[i])


num = [1,2,3,4,5,9,8]
print(num)
print(num[3])
num.sort()
#print(num1)
print(num)
num.reverse()
print(num)
print(num[0:])
print(num[::2])
print(num[::-1])
num.reverse()
num.append(10)
print(num)
num.insert(5,6)
num.insert(6,7)
print(num)
num.pop()
print(num)
print(max(num))
print(min(num))
print(len(num))


# tupple, it does not support any changes and comma should be present in tupple

tup = (1,2,3,4,5)
print(tup)

tup1 =(1,)
print(tup1)

#dictionary

d1 = {'sub1':'kannada','sub2':'english','sub3':'hindi'}
print(d1)
print(d1['sub1'])
d2 ={'sub1':'kannada','sub2':'english','sub3':'hindi','sub4':{'social':'history','science':'physics'}}
print(d2)
print(d2['sub4'])
print(d2['sub4']['social'])
d2['sub6']='maths'
print(d2)

del d1['sub2']
print(d1)

d1.update({'sub2':'english'})
print(d1)
d1.update({'sub2':'eng'})
print(d1)
print(' ')
print(d1.keys())
print(d1.values())

a = {'sub1':'kannada','sub2':'english','sub3':'hindi','sub4':'social','sub5':'science','sub6':'maths','sub7':'drawing','sub8':'8'}
print('enter key: ')
keys = input()
print(a[keys])