print("========== AI STUDY HUB ==========")

print("1. Smart Calculator")
print("2. CGPA Calculator")
print("3. Study Planner")
print("4. AI Assistant")
print("5. My Website")
print("6. Student Dashboard")

choice = input("\nEnter your choice (1-6): ")

if choice == "1":
    import smart_calculator

elif choice == "2":
    import cgpa_calculator

elif choice == "3":
    import study_planner

elif choice == "4":
    import ai_assistant

elif choice == "5":
    print("\nWebsite Link:")
    print("https://YOUR_USERNAME.github.io/Math---Projects/")

elif choice == "6":
    import student_dashboard

else:
    print("\nInvalid Option!")
