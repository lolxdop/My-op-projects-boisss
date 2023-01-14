a=int(input("plz enter ur first no."))
b=int(input("plz enter ur second no."))
c=int(input("plz enter ur third no."))
d=int(input("plz enter ur fourth no."))
e=int(input("plz enter ur fifth no."))

if a>b:
    temp = a
    a = b
    b = temp
else:
    a=a
    b=b

if a>c:
    temp = a
    a = c
    c = temp
else:
    a=a
    c=c
    
if a>d:
    temp = a
    a = d
    d = temp
else:
    a=a
    d=d
    
if a>e:
    temp = a
    a = e
    e = temp
else:
    a=a
    e=e

if b>c:
    temp = b
    b = c
    c = temp
else:
    b=b
    c=c
    
if b>d:
    temp = b
    b = d
    d = temp
else:
    b=b
    d=d

if b>e:
    temp = b
    b = e
    e = temp
else:
    b=b
    e=e

if c>d:
    temp = c
    c = d
    d = temp
else:
    c=c
    d=d

if c>e:
    temp = c
    c = e
    e = temp
else:
    c=c
    e=e
    
if d>e:
    temp = d
    d = e
    e = temp
else:
    d=d
    e=e
    
print(a , b , c , d , e)

dif1=b - a
dif2=c - b
dif3=d - c
dif4=e - d

misno1=b + dif1
misno2=misno1 + dif1
misno3=misno2 + dif1
    
if dif2!=dif1:
    print(a , "," , b , "," , "missing number is" , misno1 , "," , misno2 , "," , misno3)
    
if dif3!=dif1:
    print(a , "," , b , "," , misno1 , "," , "missing number is" , misno2 , "," , misno3)
    
if dif4!=dif1:
    print(a , "," , b , "," , misno1 , "," , misno2 , "," , "missing number is" , misno3)
    
if dif2 and dif3 and dif4 != dif1:
    print(a , "," , b , "," , "missing number are" , misno1 , "," , misno2 , "," , misno3)