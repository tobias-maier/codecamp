upper = 10
summe = 0
for i in range(0, upper):
    if i % 5 == 0 or i % 3 == 0:
        summe = summe + i
print(summe)