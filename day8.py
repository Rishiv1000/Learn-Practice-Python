# def greet():
#     print("Good Morning")

# greet()

# # def your_name(name):
# #     print(f"My name is {name}")

# # your_name("Rishi Verma")

# def what(name , branch):
#     print(f"{name} & {branch}")

# what(branch = "CSE", name="Rishi")

# import math

# hei = int(input("Height"))
# wei = int(input("Weight"))
# cover = 5

# def no_of_can(a , b , c):
#     print(f"{math.ceil((a*b)/c)}")

# no_of_can(hei,wei,cover)

# n = int(input("Check :"))

# def prime_check(num):
#     prime = 1 
#     for i in range(2,num-1):
#         if num % i == 0:
#             prime = 0
#     if prime == 1:
#         print("prime")
#     else:
#         print("not prime")

# prime_check(n)
        
# import logo from day8_art

from day8_art import logo
import string 
 
alphabet = list(string.ascii_lowercase)
print(logo)

def ceaser(start_text ,shift_amount , cipher_direction):
    mess_list = list(start_text)
    for i in range(0,len(start_text)):
        if mess_list[i] in alphabet:
            if(cipher_direction == "encode"):
                mess_list[i]= chr(ord(mess_list[i]) + shift_amount)
            elif(cipher_direction == "decode"):
                mess_list[i]= chr(ord(mess_list[i]) - shift_amount)  
            
    end_text = ""
    for x in mess_list:
        end_text += x
    print(f"The Encoded/Decoded Message is {end_text}.")

# ..............................................................


should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt Or type 'decode' to decrypt :\n")
    text = input("Type your message :\n").lower()
    shift = int(input("Type the shift number :\n"))
    shift = shift % 26
    ceaser(text , shift, direction)
    play = input("if you want continue type 'yes' else 'no' for end\n")
    if play =="yes":
        should_continue =True
    elif(play == "no"):
        should_continue = False
        print("Goodbye")

    








# def encrypt(message , shifting):
#     m_list = list(message)
#     for i in range(0,len(m_list)):
#         m_list[i] = chr(ord(m_list[i]) + shifting)
#     encoded = ""
#     for x in m_list:
#         encoded += x
#     print(f"The Encoded Message is {encoded}.")
 
# def decrypt(encoded , shifting):
#     m_list = list(encoded)
#     for i in range(0,len(m_list)):
#         m_list[i] = chr(ord(m_list[i]) - shifting)
#     message = ""
#     for x in m_list:
#         message += x
#     print(f"The Decoded Message is {message}.")


# if direction == "encode":
#     encrypt(text,shift)
# elif direction == "decode":
#     decrypt(text, shift)



