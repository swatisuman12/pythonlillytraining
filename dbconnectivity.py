import mariadb

conn = mariadb.connect(
    user="root",
    password="qwerty",
    host="localhost",
    port=3306,
    database="project",
)
cur = conn.cursor()
conn.autocommit = True
name = input("enter your name : ")
phone = input("Enter phone Number : ")
age = input("Enter Your Age : ")
sal = input("Enter your salary : ")
city = input("Enter your city: ")
dept = input("Enter Your Department: ")

try:
    cur.execute(
        "create table employee (name varchar(255), phone varchar(10), age int, sal int, city varchar(255), dept varchar(255));")
except Exception as y:
    print(y)
query = """insert into employee(name,phone,age,sal,city,dept) values(%s,%s,%d,%d,%s,%s)"""
record = (name, phone, int(age), int(sal), city, dept)
cur.execute(query, record)
cur.execute("select name, phone, age, sal,city,dept from employee;")
for (name, phone, age, sal, city, dept) in cur:
    print("Name:", {name}, "Phone:", {phone}, "Age:", {age}, "Salary:", {sal}, "City:", {city}, "Dept:", {dept})