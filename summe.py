from timeit import default_timer as timer

start = timer()
sum = 0
for number in range(0, 100_000_000):
    sum = sum + number
end = timer()

print(f"{round(end - start, 3)} seconds")

