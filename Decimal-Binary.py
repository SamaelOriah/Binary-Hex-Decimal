print("This is a binary to decimal converter. Enter a binary number and it will convert it to a decimal number.")
binNum=input("\n Enter your binary number: ")
powerNum=len(binNum)-1
decNum=0
for x in range(0,len(binNum)-1):
    if binNum[x]=="1":
        decNum+=2**powerNum
    powerNum-=1
print(f"That number in Decimal is {decNum}.")