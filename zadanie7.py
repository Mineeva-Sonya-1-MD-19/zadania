a= input('Как тебя зовут?')
a=len(a)
b=int(input('Сколько тебе лет?'))
if b>9:
    s=(b%10)+(b//10)
    d=(b%10)*(b//10)
else:
    s=b
    d=b
print(a, s, d)
