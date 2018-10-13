
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []
print(a)
ip = int(input("Please enter no. to retrieve less values than that:",))

for i in a:
    if(i<ip):
        b.append(i)

print(len(b))

