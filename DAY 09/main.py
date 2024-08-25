# student_scores = {
#   "Harry": 81,
#   "Ron": 78,
#   "Hermione": 99, 
#   "Draco": 74,
#   "Neville": 62,
# }
# # 🚨 Don't change the code above 👆

# #TODO-1: Create an empty dictionary called student_grades.
# student_grades = {}

# #TODO-2: Write your code below to add the grades to student_grades.👇
# score = 0
# remarks = ""

# for key in student_scores:
    
#     score = student_scores[key]
    
#     if score >= 91:
#         remarks = "Outstanding"
#     elif score >= 81:
#         remarks = "Exceeds Expectations"
#     elif score >= 80:
#         remarks = "Acceptable"
#     else:
#         remarks = "Fail"
        
#     student_grades[key] = remarks
    

# # 🚨 Don't change the code below 👇
# print(student_grades)

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------        

# travel_log = {
#     "France": {
#         "cities_visited": ["Paris", "Lille", "Dijon"],
#         "total_visits": 0
#         },
#     "Germany": {
#         "cities_visited": ["Berlin", "Stuttgart", "Hamburg"],
#         "total_visits": 1}
# }

# print(travel_log["Germany"])

# travel_log2 = [
#     {
#         "country": "France",
#         "cities_visited": ["Paris", "Lille", "Dijon"],
#         "total_visits": 0
#     },
#     {
#         "country": "Germany",
#         "cities_visited": ["Berlin", "Stuttgart", "Hamburg"],
#         "total_visits": 1
#     }
# ]

# print(travel_log2[0]["cities_visited"])

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------        

# travel_log = [
# {
#   "country": "France",
#   "visits": 12,
#   "cities": ["Paris", "Lille", "Dijon"]
# },
# {
#   "country": "Germany",
#   "visits": 5,
#   "cities": ["Berlin", "Hamburg", "Stuttgart"]
# },
# ]
# #🚨 Do NOT change the code above

# #TODO: Write the function that will allow new countries
# #to be added to the travel_log. 👇

# def add_new_country(country, visits, cities):
#     travel_log.append( {
#         "country": country,
#         "visits": visits,
#         "cities": cities,
#         }
#     )

# #🚨 Do not change the code below
# add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
# print(travel_log)
# print(travel_log[2])

from art import logo

print(logo)
print("Welcome to the secret auction program.")

keep_going = True
auction_data = {}
counter = 0

while keep_going:
    
    counter += 1
    
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    
    auction_data[f"{name}_{counter}"] = bid

    if input("Are there any other bidders? Type 'yes' or 'no'. ").lower() == "no":
        keep_going = False

highest_amount = 0
highest_bidder = ""
for key in auction_data:
    if auction_data[key] > highest_amount:
        highest_amount = auction_data[key]
        highest_bidder = str(key).split("_")[0]
        
print(f"The winner is {highest_bidder} with a bid of ${highest_amount}.")
    