ip = int(input("Please enter the number:"))
print("Divisors of given numbers are:",end = " " )

for x in range(2,ip):
   if ip%x == 0:
       print(x, end=" ")