#LAB4

#1
"""
salary = float(input("Enter salary:"))
years = int(input("Enter years:"))
if years>5 :
    bonus = salary * 0.05
else:
    bonus = 0
print("bonus", bonus)
"""

#2
"""
p = input("Enter pass:")
if p == "s3cr3t!P@ssw0rd" :
    print ("Welcome")
else:
    print ("Wrong Password!")
"""
#4
"""

h = int(input("Enter hours:"))
m = int(input("Enter minutes:"))
m = m + 15
if m>=60:
    m = m-60
    h = h+1
if h==24:
    h=0
if m<10:
    print(h,":0", m)
else : 
    print(h,":", m) 
"""
#5
"""
n = float(input("Enter kms:"))
t = input("Enter day or night:")
if t == "day":
    taxi = 33.58+n*37.89
else:
    taxi = 33.58+n*43.17
    cheapest = taxi
if n>=20:
    bus=n*4.32
if bus<cheapest:
    cheapest = bus
if n>=100:
    train=n*2.68
if train<cheapest:
    cheapest=train
print("Chepest price=", cheapest)
"""

#6
"""
h=int(input("Enter holidays:"))
w=365-h
wm=w*63
hm=h*127
total=hm+wm

if total<=30000:
    diff=30000-total
    print("Tom sleeps well")
    print("difference=", diff)
else:
    diff=total-30000
    print("Tom does not sleep well")
    print("difference", diff)
"""

#7
"""
b=float(input("Enter budget: "))
s=input("Enter season: ")
if b<=100:
   d="Bulgaria"
if s=="summer":
   p="Camping"
   m=b*30/100
else:
   p="Hotel"
   m=b*70/100
elif b<=1000:
    d="Balkans"
if s=="summer":
       p="Camping"
       m=b*40/100
else:
    p="Hotel"
    m=b*80/100
else:
    d="Europe"
    p="Hotel"
    m=b*90/100
print("Destination:",d)
print("Place:",p)
print("Money spent:",m)
"""
#8
"""
for i in range(1,1001):
    if i%10==6:
        print(i)
"""
#9
"""
n=int(input("Enter n: "))
s=0
for i in range(n):
    x=int(input("Enter number: "))
    s=s+x
print("Sum =",s)
"""
#10
"""
n=int(input("Enter number: "))
for i in range(1,21):
    print(n,"x",i,"=",n*i)
"""
