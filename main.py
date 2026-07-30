import os

print("====== AI STUDY HUB ======")
print("1. Smart Calculator")
print("2. CGPA Calculator")
print("3. Study Planner")
print("4. AI Assistant")
print("5. My Website")

choice = input("Select an option (1-5): ")

if choice == "1":
    os.system("python smart_calculator.py")

elif choice == "2":
    os.system("python cgpa_calculator.py")

elif choice == "3":
    os.system("python study_planner.py")

elif choice == "4":
    os.system("python ai_assistant.py")

elif choice == "5":
    print("Opening Website...")

else:
    print("Invalid option!")