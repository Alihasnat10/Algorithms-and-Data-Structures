def bonAppetit(bill, k, b):
    bill.pop(k)
    total = 0
    for i in range(len(bill)):
        total += bill[i]
    total = total / 2
    if total == b:
        print('Bon Appetit')
    else:
        print(int(b - total))

k = 1
bill = [3, 10, 2, 9]
b = 12
bonAppetit(bill, k, b)
