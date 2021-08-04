#READING FILES

f= open('test.txt', 'r')
print(f.read())

#write
f= open('test.txt', 'w')
f.write(' hello world')


f= open('test.txt', 'r')
print(f.read())