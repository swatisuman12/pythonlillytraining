'''
'r': read file
'w': write file
'x': if there is no file,it creats file but file is already
'a': append the file
't': text
'b': binary mode
'r+': read and write
f = open('sample.txt')
content = f.read(5)
print(content)
contents = f.read(6) # reads next 5 characters
print(contents)
line = f.readline(5)
print(line)
f.close()
f= open('sample.txt','a')
sam= f.write('sample program 2\n') # write function doesnot appends, it overwrites
print(sam)
f.close()
'''
f = open('sample.txt')
print(f.readline())
print(f.readline())
f.seek(8)
print(f.readline())
f.close()