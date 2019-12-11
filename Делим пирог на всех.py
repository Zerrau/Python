a=int(input())
b=int(input())
i=1
d=0
while i <= (a+b):
    d = a * i
    i += 1
    if d % a == 0 and d % b == 0:
        print(d)
        break


