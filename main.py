from math_quiz import math_quiz
from english_quiz import english_quiz
from science_quiz import science_quiz


def clear():
    print("\n" * 3)


def line():
    print("=" * 55)


def menu():
    while True:
        clear()
        line()
        print("🤖          AI QUIZ GENERATOR")
        line()
        print("1. Mathematics Quiz")
        print("2. English Quiz")
        print("3. Science Quiz")
        print("4. About Project")
        print("5. Exit")
        line()

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            math_quiz()

        elif choice == "2":
            english_quiz()

        elif choice == "3":
            science_quiz()

        elif choice == "4":
            clear()
            line()
            print("AI QUIZ GENERATOR")
            line()
            print("A professional quiz application built")
            print("using Python.")
            print()
            print("Features:")
            print("✔ Mathematics Quiz")
            print("✔ English Quiz")
            print("✔ Science Quiz")
            print("✔ Automatic Score")
            print("✔ Percentage")
            print("✔ Grade")
            print("✔ Motivational Message")
            line()
            input("Press Enter to return to Menu...")

        elif choice == "5":
            clear()
            line()
            print("Thank you for using AI Quiz Generator!")
            print("Good Luck with your studies.")
            line()
            break

        else:
            print("\nInvalid Choice!")
            input("Press Enter...")


menu()