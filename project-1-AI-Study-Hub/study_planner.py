print("===== STUDY PLANNER =====")

name = input("Enter your name: ")
hours = int(input("How many hours will you study today? "))

print("\n----- Today's Plan -----")
print("Name:", name)
print("Study Hours:", hours)

if hours >= 8:
    print("Excellent! Keep it up.")
elif hours >= 5:
    print("Good job! You are doing well.")
else:
    print("Try to study more tomorrow.")

print("\nBest of luck!")
