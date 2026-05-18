go = False
while go==False:
    try:
        age = input("Enter your age: ")
        age = int(age)
        go = True
    except:
        go = False
        print("Only whole numbers are accepted!")
print(f"You were born in {2026-age}")