# no =int(input("Enter Number"))

# if ((no%2 == 0)):
#     print("even")
# else:
#     print("odd")    


# height = int(input("whats your height in cm."))
# weight = int(input("whats your weight in kg"))

# bmi =  round(weight/height**2)

# if bmi <18.5:
#     print("underweight")
# elif bmi<25:
#     print("normal")
# elif bmi <30:
#     print("overwight")
# elif bmi <35:
#     print("obese")
# else:
#     print("clicnincly obese")            


# year = int(input("Enter Year"))

# if year%4 == 0:
#     if year%100==0:
#         if year%400 ==0:
#             print("Leap")
#         else:
#             print("not")  
#     else:
#         print('leap')
# else:
#     print("not leap")       
   
   
 
# print("welcome to pizZA")
# size = input("what size S , M ,L")
# add_memo = input("Y or N")
# extra = input("cheese Y or N")

# price =0

# if size == "S":
#     price += 15
# elif size == "M":
#     price += 20
# else:
#     price += 25


# if add_memo == "Y":
#     if size== "S":
#         price+=2
#     else :
#         price+=3

# if extra =="Y":
#     price+=1

# print(f"full price {price}")    


 
name1 = input("FIRST NAME\n")
name2 = input("SECOND NAME\n")
 

name_full = name1 + name2
namelower = name_full.lower() 


t = namelower.count("t")
r = namelower.count("r")
u = namelower.count("u")
e = namelower.count("e")
 
l = namelower.count("l")
o = namelower.count("o")
v = namelower.count("v")
e = namelower.count("e")

true = t+u+r+e
love = l+o+v+e

pre = str(true) + str(love)
print(pre)