# dic = {
#     "Name" : "Rishi Verma",
#     "Class": 9
# }
# print(dic["Name"])

# stu_score = {
#     "Harry" :81,
#     "Ron" : 78,
#     "Hermione": 99,
#     "Draco":74,
#     "Neville": 62
# }

# stu_grade = {}

# for x in stu_score:
#     score = stu_score[x]
#     if score > 90:
#         stu_grade[x] = "Outstanding"
#     elif score > 80:
#         stu_grade[x] = "Exceeds Expectation"
#     elif score > 70:
#         stu_grade[x] = "Acceptable"
#     else :
#         stu_grade[x] = "fail"

# print(stu_grade )

# travel_log = [{
#     "country" :"France",
#     "visits": 12,
#     "cities" : ["Paris", "Lille","Dijon"]
# },{
#     "country" :"Germany",
#     "visits": 5,
#     "cities" : ["Berlin" ,"Hamburg"]
# }]



# def add_new_country(countrys , visit_times, listofcity ):
#     travel_log.append({
#     "country" : countrys,
#     "visits" : visit_times,
#     "cities" : listofcity
#     })

# add_new_country("Russia", 2 , ["moscow", "sait"])
# print(travel_log)

# print(len(travel_log))


newbider = {} 
ender = True
 
def compare(record):
    higher = 0
    for x in record:
        bidamount = record[x]
        if bidamount > higher:
            higher = bidamount
            winner = x

    print(f"WINNER IS {winner} & Highest is {higher}")


while ender:
    name = input("what is your name ?\n")
    price = int(input("type you bid ? $"))
    newbider[name] = price
    should_continue = input("Continue 'yes' else 'no'\n")
    if should_continue == "no":
        ender = False
        compare(newbider)
    elif should_continue == "yes":
        print("Continud Biding")







