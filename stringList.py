ip = input("Please enter the Sting:")

for i in range(0 ,int(len(ip)/2)):
    if(ip[i] ==ip[-i-1]):
        flag = True
    else:
        flag = False
        break

    

if(flag  == True):
    print("String is Pallingdrome")
    
else:
    print("String is not Pallingdrome")