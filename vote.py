age=int(input("Enter age: "))
if(age>=18):
    print("You are eligible for voting")
elif(age==0):
    print("invalid age.")
else:
    age2 = 18-age
    #you can change 2024 as per current year!
    year = 2024 + age2
    print(f"You are eligible after {age2} year in {year} year.")
