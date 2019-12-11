A = int(input())
B = int(input())
H = int(input())
if A <= H <= B:
    print("Это нормально")
elif A > H < B:
    print("Недосып")
elif B <= H > A:
    print("Пересып")