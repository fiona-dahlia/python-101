goal = int(input("How high should I count? "))
start = int(input("Where should I start? "))
interval = int(input("What should I count by? "))

for i in range(start, goal + 1, interval):
    print(i)
