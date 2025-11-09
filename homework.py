print("Let's count some numbers!")

how_many = 0

while True:
    number = input("Type a number (or 'stop' to end): ")

    if number == "stop":
        break
    
    how_many = how_many + 1

print("You typed", how_many, "numbers!")
