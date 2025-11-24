#Study Time Tracker
#This program asks how many hours the user studied today
#Estimates their weekly study hours.

print("Welcome to my Python program!")

#ask user for input
hours = input("How many hours did you study today? ") 

try:
    #converting the input to a float
    hours = float(hours)
except ValueError:
    #If the user types something thats not necessary, an error will show
    print("Please enter a valid number for hours studied.")
    exit()

#Calculate weekly hours
weekly_hours = hours * 7 

#Display the result to the user
print(f"You are on track to study {weekly_hours} hours this week!")

