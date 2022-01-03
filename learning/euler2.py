# 1 2 3 5 8 13
current = 1
next = 2
summe = 0
while current < 100_000_000:
    next, current = current + next, next
    if current % 2 == 0:
        summe += current
print(summe)