# fruits = ["Apple", "Banana","Pea"]

# for fruit in fruits:
#     print(fruit)


# stu_height = input("Enter Heights\n")

# Heights = stu_height.split()

# for n in range(0, len(Heights)):
#     Heights[n] = int(Heights[n])

# print(Heights)

# i=0
# for x in Heights:
#     i += x
# print(i)    


# y = 0
# for x in Heights:
#     y +=1
# print(y)  

# avg = round(i/y)
# print(avg)



# score = input("Enter Number").split(',')
# for n in range(0,len(score)):
#     score[n]=int(score[n])

# max = 0
# for x in score:
#     if max < x:
#         max = x
# print(max)

# total = 0
# for i in range(1,101):
#     if(i%2)==0:
#         total+=i
# print(total)


# for i in range(1,101):
#     if  ((i%3)==0)and ((i%5)==0):
#         print("fizz")
#     elif(i%5)==0:
#         print("Buzz")
#     elif ((i%3)==0):
#         print("fizzbuzz")    
#     else:
#         print(i)

import random

letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

Number  = ['0','1','2','3','4','5','6','7','8','9'] 

symbol = ['!',"@", "#","$","%"]

print("WELCOME TO PASSWORD GENERATOR")

letters = int(input("How lettwrs in  your password"))
symbols = int(input("How symbol in your password"))
numbers = int(input("How numbers your password"))


# password = ""

# for l in (1 , letters+1):
#     password += random.choice(letter)
# for s in range(1,symbols+1):
#     password += random.choice(symbol)   
# for n in range(1, numbers+1):
#     password +=random.choice(Number)
# print(password)
     
pass_list = []

for l in (1 , letters+1):
    pass_list.append(random.choice(letter))
for s in range(1,symbols+1):
    pass_list.append(random.choice(symbol))   
for n in range(1, numbers+1):
    pass_list.append(random.choice(Number))


print(pass_list)

random.shuffle(pass_list)
print(pass_list)

password = ""

for char in pass_list:
    password += char

print(password)
