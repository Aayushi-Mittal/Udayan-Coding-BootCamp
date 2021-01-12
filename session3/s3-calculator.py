# Calculator using if-else statements
num1=int(input("Enter first number : "))
num2=int(input("Enter second number : "))
choice=input("Enter your choice (+, -, *, /, %, ^) : ")
if(choice=='+') :
    print(num1+num2)
elif(choice=='-') :
    print(num1-num2)
elif(choice=='*') :
    print(num1*num2)
elif(choice=='/') :
    print(num1/num2)
elif(choice=='%') :
    print(num1%num2)
elif(choice=='^') :
    print(num1**num2)
else :
    print("Invalid Choice!")
    
# num1 + "^" + num2 + " = " + (num1**num2)