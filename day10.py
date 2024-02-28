# def format_name(f_name , l_name):
#     full_name = f_name.title() +" " l_name.title()
#     return full_name

# first = input("Your First Name \n")
# second = input("Your Second Name \n")

# a = format_name(first, second)
# print(a)




# def leap(year):
#     if year%4 == 0:
#         if year%100==0:
#             if year%400 ==0:
#                 return True
#             else:
#                 return False
#         else:
#             return True
#     else:
#         return False

# def days_in_month(Year,Month):
#     month_days = [31,28,31,30,31,30,31,30,31,30,31,30]
#     if leap(Year) and Month == 2:
#         return 29
#     return month_days[Month-1]


# year = int(input("Enter Year\n"))
# month = int(input("Enter Month\n"))
# days = days_in_month(year,month)
# print(days)


def add(n1 ,n2):
    return n1 + n2

def sub(n1,n2):
    return n1 - n2

def mul(n1 ,n2):
    return n1 * n2

def div(n1 , n2):
    return n1 / n2


op = {
    "+" : add,
    "-" : sub,
    "*" : mul ,
    "/" : div
 }


def calculation():
    n1 = int(input("What first no.\n"))
    for i in op:
        print(i)
    should_con = True
    while should_con:
        op_symbol = input("Pick On Operation\n")
        n2 = int(input("What second no.\n"))

        cal = op[op_symbol]
        answer = cal(n1,n2)

        print(f"{n1} {op_symbol} {n2} = {answer}")

        if input(f"type y for continue\n or type new for new calculation")== 'y':
            pre =answer
        else :
            should_con = False
            calculation()

calculation()

# op_symbol2 = input("Pick Another Operation")
# n3 = int(input("Enter New Value")) 
# cal = op[op_symbol]
# answer2 = cal(answer,n3 )
# print(f"{answer} {op_symbol} {n3} = {answer2}")



