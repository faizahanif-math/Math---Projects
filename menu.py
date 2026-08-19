# ----- AI STUDENT ASSISTANT MAIN MENU -----

print("\n====================================")
print("       AI STUDENT ASSISTANT")
print("====================================")

while True:

    print("\n----------- MAIN MENU -----------")
    print("1. Student Dashboard")
    print("2. Smart Study Planner")
    print("3. Study Progress Tracker")
    print("4. CGPA Calculator")
    print("5. Study Recommendation")
    print("6. Performance Analysis")
    print("7. Exit")
    print("--------------------------------")

    choice = input("Enter your choice (1-7): ")

    if choice == "1":
        print("\nStudent Dashboard selected ✅")

    elif choice == "2":
        print("\nSmart Study Planner selected 📚")

    elif choice == "3":
        print("\nStudy Progress Tracker selected 📊")

    elif choice == "4":
        print("\nCGPA Calculator selected 🧮")

    elif choice == "5":
        print("\nStudy Recommendation selected 🎯")

    elif choice == "6":
        print("\nPerformance Analysis selected 📈")

    elif choice == "7":
        print("\nThank you for using AI Student Assistant! 👋")
        break

    else:
        print("\nInvalid choice. Please enter a number from 1 to 7")
        