print("This is a binary to decimal converter. Enter a binary number and it will convert it to a decimal number.")
binNum=input("\nEnter your binary number: ")
oneCount=0
zeroCount=0
synCorrect=False
while synCorrect==False:
    for x in binNum:
        if x=="1":
            oneCount+=1
        elif x=="0":
            zeroCount+=1
    if oneCount+zeroCount!=len(binNum):
        print("Binary numbers can only contain 1s or 0s. Try again.")
        binNum=input("\nEnter your binary number: ")
    else:
        synCorrect=True
powerNum=len(binNum)-1
decNum=0
for x in range(0,len(binNum)-1):
    if binNum[x]=="1":
        decNum+=2**powerNum
    powerNum-=1
print(f"That number in Decimal is {decNum}.")