print("Welcome to the tip calculator") 

total_bill = input("What was the total bill ?")

bill = float(total_bill)

precen = input("Give % 10 or 12 or 15 ?")

pre = int(precen)

people = input("Peoples are ?")

peo = int(people)

tot_pre = (bill*pre)/100  

total_split = tot_pre + bill

print(f"Each person should pay : {total_split}")