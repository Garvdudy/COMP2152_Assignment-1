"""
Author: Garv
Assignment: #1
"""

#-----------------------------------------------------------

# Step b: Create 4 variables
#string variable
gym_member = "Alex Alliton"  #str

#float variable
preferred_weight_kg = 20.5  #float

#integer variable
highest_reps = 25  # int

#boolean variable
membership_active = True  #bool

#-----------------------------------------------------------

# Step c: Create a dictionary named workout_stats
#dictionary with string keys & tuple values (int, int, int)
workout_stats = {
    "Alex": (20, 35, 40),     #yoga, running, weightlifting
    "Daksh": (30, 45, 35),
    "Tushar": (30, 60, 40)
}

#-----------------------------------------------------------

# Step d: Calculate total workout minutes using a loop and add to dictionary
for friend, minutes in list(workout_stats.items()):
    total_minutes = sum(minutes)
    workout_stats[f"{friend}_Total"] = total_minutes

#-----------------------------------------------------------

# Step e: Create a 2D nested list called workout_list
#2D list (list of lists) storing workout minutes
workout_list = [
    list(workout_stats["Alex"]),
    list(workout_stats["Daksh"]),
    list(workout_stats["Tushar"])
]

#-----------------------------------------------------------

# Step f: Slice the workout_list
print("Yoga and Running minutes for all the friends -->")
for row in workout_list:
    print(row[0:2])
print("--------------------------------------------------")
print("Weightlifting minutes for the last two friends -->")
for row in workout_list[-2:]:
    print(row[2])

#-----------------------------------------------------------

# Step g: Check if any friend's total >= 120
for friend in ["Alex", "Daksh", "Tushar"]:
    total = workout_stats.get(f"{friend}_Total")
    if total >= 120:
        print(f"Great job staying active, {friend}!")
    else:
        print(f"Catch up, {friend}!!!")

#-----------------------------------------------------------

# Step h: User input to look up a friend
name = input("Enter Friend's Name: ")

if name in workout_stats:
    yoga, running, weightlifting = workout_stats[name]
    total = workout_stats[f"{name}_Total"]

    print(f"\nWorkout details for {name}:")
    print(f"Yoga: {yoga} Minutes")
    print(f"Running: {running} Minutes")
    print(f"Weightlifting: {weightlifting} Minutes")
    print(f"Total: {total} Minutes")
else:
    print(f"Friend {name} not found in the records.")

#-----------------------------------------------------------

# Step i: Friend with highest and lowest total workout minutes
totals = {
    "Alex": workout_stats["Alex_Total"],
    "Daksh": workout_stats["Daksh_Total"],
    "Tushar": workout_stats["Tushar_Total"]
}

highest = max(totals, key=totals.get)
lowest = min(totals, key=totals.get)

print(f"\nHighest total workout minutes: {highest}")
print(f"Lowest total workout minutes: {lowest}")