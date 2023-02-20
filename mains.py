import operators

import trig
num1=eval(input("Enter number1:"))
num2=eval(input("Enter number2:"))
operator=input("Enter operator:")

if operator=="+":
    x=operators.add(num1, num2)
    print(x)
elif operator=="-":
    y=operators.subtract(num1, num2)  
    print(y)  
elif operator=="/":
     z=operators.divide(num1, num2)
     print(z)
elif operator=="*":
     a=operators.multiply(num1, num2)
     print(a)    
elif operator=="sin":
     angle=eval(input("Enter degrees:"))
     sin_of_angle=trig.get_sine(angle)
     print(sin_of_angle)

elif operator=="cos":
     angle=eval(input("Enter degrees:"))
     print(trig.get_cos(angle))


