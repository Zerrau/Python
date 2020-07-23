# Напишите программу, которая принимает на вход список чисел в одной строке и выводит на экран в одну строку значения,
# которые повторяются в нём более одного раза.
# Для решения задачи может пригодиться метод sort списка.
# Выводимые числа не должны повторяться, порядок их вывода может быть произвольным.

a = input()
a = a.split()
num = len(a)

a = list(map(int, a))
a = sorted(a)

ind = 0
ind2 = 1
ans = []

if num <= 1:
    pass
else:
    for i in a:
        if ind2 == num:
            break
        if a[ind] == a[ind2]:
            ans.append(a[ind])
        ind = ind + 1
        ind2 = ind2 + 1

ans = list(dict.fromkeys(ans))

print (" ".join(map(str, ans)))

