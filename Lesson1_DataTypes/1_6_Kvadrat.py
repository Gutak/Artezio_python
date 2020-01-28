# 6. Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x). 
# Sample Dictionary ( n = 5) :
# Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

n = input("Введите число n = ")
n = int(n)

d = dict()

# от 1 до n
for x in range(1, n+1):
    d[x] = x*x
print(d)