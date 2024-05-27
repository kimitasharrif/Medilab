# function to add two  numbers
#  1.functions without parameters
def add():
    num1 =50
    num2 = 40
    answer=num1 +num2
    print(answer)

# call/invoke
add()
    
def SI():
    p =1000
    r =5
    t =3 
    si=  p*r*t/100
    print(si)
SI()

# 2. functions with parameters
# add two numbers
def SI(p, r, t):
    si= p* r* t/100
    print(si)

SI(2354,2,5)    

def sum(num1, num2):
    sum=num1+num2
    print(sum)
sum(20, 30)
sum(23,432)
    
# BMI
def BMI(weight, height):
  bmi = weight/(height*height)
  print(bmi)
    
BMI(20,40)

#Area of a circle
def AOC(radius):
    aoc = 22/7*radius*radius
    print(aoc)
AOC(7)    
#  3.function to check which number is greater 
# given x and y

# def num(x, y):
#    if x > y :
#         print("x greater than y")
  
#    else:
#         print("y is greater than x")

# num(2, 3)        


# def num(x, y ,z):
#    if x > y/z :
#         print("x greater than y and z")
#    elif y > x/z:
#        print("y greater than x and z")
#    elif z > x/y:
#        print("z greater than x and y")        
#    else:
#         print("y, x, z are equal")

# num(23,48,3)        
# num(23,23,23) 



# WRITE A FUNCTION TO CHECK IF ODD or even NUMBERS
def odd(num):
    
    if num % 2==1: #% 2 !=0
        print( num ,"the number is odd")
    else:
        print(num,"the num is even")    


odd(22)



