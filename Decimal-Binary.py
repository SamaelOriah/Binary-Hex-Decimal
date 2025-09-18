print("In this section we will convert a Decimal to a Binary number")
powerNum=0
binNum=[]
highNumFound=False
decNum=int(input("Please enter your decimal number: "))
while highNumFound==False:
    if decNum-(2**powerNum)<0:
        highNumFound=True
    else:
        powerNum+=1
    
decNum-=2**powerNum
binNum.append(1)
powerNum-=1
while powerNum>=0:
    if decNum-2**powerNum>0:
        binNum.append(1)
        decnum-=2**powerNum
        powerNum-=1
    else:
        binNum.append(0)
        powerNum-=1
for x in binNum:
    print(x, end="")
print("")


