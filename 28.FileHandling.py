
f=open("text.txt","w")
userInput=input("Enter a number :")
userInput1=input("Enter a number :")
f.write(userInput+"\n")
f.write(userInput1+"\n")
f=open("text.txt","r")
num1=int(f.readline())
num2=int(f.readline())
print(num1+num2)