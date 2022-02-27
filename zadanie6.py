a=input('Как тебя зовут?')
b=''
c=''
f=a[1:]
f=f[:-1]
f=f[::-1]
s=len(a)
b=a[s-3:]
c=a[:5]
print(f, b, c)
