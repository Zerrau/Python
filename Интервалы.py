a = int(input())
b = a + 1  # Бесконечность b всегда больше а
if -15 < a <= 12:
    print("True")
elif 14 < a < 17:
    print("True")
elif 19 <= a < b:
    print("True")
else:
    print("False ")