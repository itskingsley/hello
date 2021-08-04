x = "Kshs.2,450.00"
y = "John Omondi"
import datetime
z = datetime.datetime.now()
k = "Kshs.6,593.00"
h = "PGTRQ2WJQT confirmed " + x
t = " \t paid to "+y
u = " on" 

f = " \n . New balance is "+k
#print(h + t + u +f)


import re

test_testing = "123ABC123MNOabc123"
w = re.findall('123$', test_testing)
#print(w)
g =  re.search('123', test_testing)
#print(g)

l = re.finditer('123', test_testing)
#for items in l:
    #print(l)
match = re.match('123', test_testing)
print(match.group())
match = re.match('123', test_testing)
print(match.end())
AGE =  30

if AGE >  100: 
    print('He is  an adult')
elif AGE == 30:
    print('where have you been')
elif AGE < 18 :
    print('You are minor')
B = (1, 3 ,43, 45 ,45)  
A = set(B)
print(A)

#try:
   # print(hj)
  
#except NameError as e:
   # print(e)
#finally:
   # print('i will execute despite')
try:
    f = open('test.txt', w)
     f.close()
    
except :
    print('dxvfv')

    