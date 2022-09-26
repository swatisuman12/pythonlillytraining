x = input("Enter your first name: ")

while (True):

    if len(x) > 0 :
        if x.isalpha()==True:
           print("Your First name is: ", x)  
        
        if x.isalpha()== False:
            print(input("enter your name again: "))
            break