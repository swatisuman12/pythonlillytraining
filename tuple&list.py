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