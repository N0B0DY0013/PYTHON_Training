
# numbers = [1, 2, 3]
# print([n + 1  for n in numbers])

# print([n * 2 for n in range(1, 5)])

# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# print([name.upper() for name in names if len(name) >= 5])

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# 🚨 Do Not Change the code above 👆

#Write your 1 line code 👇 below:
squared_numbers = [n**2 for n in numbers]
even_numbers = [n for n in numbers if n % 2 == 0]

#Write your code 👆 above:
print(f"Squared Numbers: {squared_numbers}")
print(f"Even Numbers: {even_numbers}")

with open("file1.txt") as file_1:
    with open("file2.txt") as file_2:
        file_1_data = file_1.readlines()
        file_2_data = file_2.readlines()
        
        print(f"Common Numbers in File1.txt and File2.txt: {[int(num.strip()) for num in file_1_data if num in file_2_data]}")