# Make a progrm which prints a multiplication table

"""
1.0
test = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(len(test)):
    print(i * 2)

2.0
test = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in test:
    print(i * 2)



3.0
def times(x):
    return(x * 0, x * 1, x * 2, x * 3, x * 4, x * 5, x * 6, x * 7, x * 8, x * 9, x * 10)


test = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

halfway = map(times, test)

result = list(halfway)

print(result)


4.0
def times(x):
    return(x * 0, x * 1, x * 2, x * 3, x * 4, x * 5, x * 6, x * 7, x * 8, x * 9, x * 10)


test = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

halfway = map(times, test)

result = list(halfway)

for item in result:
    print(item)

"""

#5.0 - FINAL

def times(x):
    return [x * i for i in range(11)]


test = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

halfway = map(times, test)

result = list(halfway)

for item in result:
    print(item)
