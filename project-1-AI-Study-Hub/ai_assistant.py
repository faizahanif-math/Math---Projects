print("===== AI STUDY HUB =====")

print("1. Smart Calculator")
print("2. CGPA Calculator")
print("3. Study Planner")
print("4. AI Assistant")

choice = input("Select an option (1-4): ")

if choice == "1":
    print("Opening Smart Calculator...")

elif choice == "2":
    print("Opening CGPA Calculator...")

elif choice == "3":
    print("Opening Study Planner...")

elif choice == "4":
    print("Welcome to AI Assistant!")
    question = input("Ask me anything: ")
    print("You asked:", question)
    print("Thank you for using AI Assistant.")

else:
    print("Invalid option!")
