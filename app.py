print("Welcome to my Python program!")

hours = input("How many hours did you study today? ") #ask user for input

try:
    #Try converting the input to a number
    hours = float(hours)
except ValueError:
    #If the user types something invalid, show an error and exit
    print("Please enter a valid number for hours studied.")
    exit()

weekly_hours = hours * 7 #Calculate weekly hours

print(f"You are on track to study {weekly_hours} hours this week.") #Display the result to the user

