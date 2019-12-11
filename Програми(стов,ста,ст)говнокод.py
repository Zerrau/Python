n = int(input())
if (n > 10 and n < 15) or (n > 110 and n < 115) or (n > 210 and n < 215) or (n > 310 and n < 315) or (
        n > 410 and n < 415) or (n > 510 and n < 515) or (n > 610 and n < 615) or (n > 710 and n < 715) or (
        n > 810 and n < 815) or (n > 910 and n < 915):
    print(n, "программистов")
elif 4 >= n >= 2 or (n % 10) == 2 or (n % 10) == 3 or (n % 10) == 4:
    print(n, "программиста")
elif n == 1 or (n % 10) == 1:
    print(n, "программист")
else:
    print(n, "программистов")


