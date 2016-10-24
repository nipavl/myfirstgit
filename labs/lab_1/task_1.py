import math
import random

MyVarA = input('insert a = ')
print(MyVarA, MyVarA, 'fkdkkd')



print("Test 1 Елементарні оператори ")
a = int(input("Введiть a:"))
x = int(input("Введiть x:"))
c = int(input("Введiть c:"))
result =(math.sqrt((math.e**x)-math.cos(x*x*(a**5))**4)+math.atan(a-x**5)**4)/math.sqrt(math.fabs(a+x*(c**4)))

print("Test 2 Умовні оператори ")

a = float(input("Введiть a:"))
b = float(input("Введiть b:"))
c = float(input("Введiть c:"))
d = float(input("Введiть d:"))

x = float(input("Введiть x:"))
y = float(input("Введiть y:"))
z = float(input("Введiть z:"))
V = 0

if (a<=b and c<=d) :
    if (x>c and y>c and z>c and x<d and y<d and z<d ): V=max(x,y,z)
elif (x>c and y>c and z>c and x>d and y>d and z>d ): V=min(x,y,z)
else:V=(a+b)/2
print("V=",V)
else : print("Введені дані, які не відповідають початковій умові")


print("Test 3 Циклічні оператори ")

x = float(input("Введiть x:"))
a = float(input("Введiть a:"))
e = float(input("Введiть e:"))

k=0
kfac=0
if (a!=0 and x!=0 and e>0):
res= (((-1)**k)*math.log2(x**(2*k)))/(a**k+ kfac)
k+=1
kfac+=1
res1 = (((-1) ** k) * math.log2(x ** (2 * k))) / (a ** k + kfac)

while (e<(res-res1)):
res = res1
k+=1
kfac+=1
res1 = (((-1) ** k) * math.log2(x ** (2 * k))) / (a ** k + kfac)

print("Cумма=", res1)
print("Кількість доданків=", k)

 else : print("Введені некоректні дані")


print("Test 4 Масиви ")

n = int(input("Введіть розмірність масиву:"))
a = float(input("Введiть a:"))
b = float(input("Введiть b:"))
random.seed()
list = []
sum=0
multiple=1
max=a
min=b
for i in range(n):
list.append(random.randint(-100,100))
print(list[i]) 
if list[i]< a :
 sum+=list[i]
 elif list[i]> b :
 multiple*=list[i]
 else:
 if list[i]<min:
 min=list[i]
if list[i]>max :
 max=list[i]

if max==a:
print("Чисел в проміжку [a,b] не виявлено")
else : print("min= ",min," max= ",max)

if sum==0: ("Чисел менших а не виявлено")
else: print("Sum= ",sum)

if sum==0: ("Чисел більших b не виявлено")
else: print("Добуток= ",multiple)




print("Test 5 Робота з текстом ")

text = (input("Введіть текст який потрібно обробити "))
splitText=[]
splitText=text.split(" ")
mn = {"!",".",",","?",":",}
textwithWWord=""
textwithoutWWord=""

for s in splitText:
b = True
if s[len(s)-1] in mn:
s=s[0:len(s)-1]
for k in range(len(s)-1):
if (s[k+1]== s[k]):
b=False
break
if b :
textwithoutWWord+=s+" "
else: textwithWWord+=s+" "

print(textwithoutWWord)
print(textwithWWord)