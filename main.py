print("===================================")
print("   AI STUDENT ASSISTANT")
print("===================================")

name = input("Enter your name: ")
semester = input("Enter your semester: ")
field = input("Enter your field: ")

print("\n------ Student Profile ------")
print("Name:", name)
print("Semester:", semester)
print("Field:", field)
print("-----------------------------")

print("\nWelcome,", name + "!")
print("Your AI Student Assistant is ready.")
print("\n===================================")
print("       SMART STUDY PLANNER")
print("===================================")

subjects = []

number = int(input("\nHow many subjects do you want to add? "))

for i in range(number):
    subject = input(f"Enter subject {i + 1}: ")
    subjects.append(subject)

print("\n------ Your Study Plan ------")

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

for i, subject in enumerate(subjects):
    day = days[i % len(days)]
    print(f"{day}: Study {subject}")

print("-----------------------------")
print("Study plan created successfully!")
print("\n===================================")
print("       STUDY PROGRESS TRACKER")
print("===================================")

subject = input("\nEnter subject name: ")
total_topics = int(input("Enter total topics: "))
completed_topics = int(input("Enter completed topics: "))

if total_topics > 0 and 0 <= completed_topics <= total_topics:
    progress = (completed_topics / total_topics) * 100

    print("\n------ Progress Report ------")
    print("Subject:", subject)
    print("Total Topics:", total_topics)
    print("Completed Topics:", completed_topics)
    print(f"Progress: {progress:.1f}%")

    if progress >= 80:
        print("Status: Excellent progress! 🌟")
    elif progress >= 50:
        print("Status: Good progress! 👍")
    else:
        print("Status: Keep working! 📚")
else:
    print("Invalid input. Please check your numbers.")
    # ----- CGPA CALCULATOR -----

print("\n==============================")
print("       CGPA CALCULATOR")
print("==============================")

subjects = int(input("Enter number of subjects: "))

total_points = 0
total_credits = 0

for i in range(subjects):
    print(f"\nSubject {i + 1}")
    grade_point = float(input("Enter grade point (0-4): "))
    credit_hours = float(input("Enter credit hours: "))

    total_points += grade_point * credit_hours
    total_credits += credit_hours

if total_credits > 0:
    cgpa = total_points / total_credits

    print("\n----- CGPA RESULT -----")
    print(f"Your CGPA: {cgpa:.2f}")

    if cgpa >= 3.5:
        print("Status: Excellent! 🌟")
    elif cgpa >= 3.0:
        print("Status: Good! 👍")
    elif cgpa >= 2.0:
        print("Status: Keep working! 💪")
    else:
        print("Status: Needs improvement.")
else:
    print("Invalid credit hours.")
    # ----- STUDY RECOMMENDATION SYSTEM -----

print("\n==============================")
print("    STUDY RECOMMENDATION")
print("==============================")

weak_subject = input("Enter your weak subject: ")
study_hours = float(input("How many hours can you study daily? "))

print("\n----- Personalized Recommendation -----")

if study_hours >= 4:
    print(f"Focus strongly on {weak_subject}.")
    print("Recommended: 2 hours concepts + 1 hour practice + 1 hour revision.")
elif study_hours >= 2:
    print(f"Give extra attention to {weak_subject}.")
    print("Recommended: 1 hour concepts + 1 hour practice.")
else:
    print(f"Start with {weak_subject} for at least 30 minutes daily.")
    print("Focus on important concepts and short practice sessions.")

print("\nStudy recommendation created successfully! 🎯")
# ----- PERFORMANCE ANALYSIS -----

print("\n==============================")
print("     PERFORMANCE ANALYSIS")
print("==============================")

performance_cgpa = float(input("Enter your current CGPA (0-4): "))
progress = float(input("Enter your study progress percentage: "))

print("\n----- Performance Report -----")

if performance_cgpa >= 3.5 and progress >= 75:
    print("Overall Performance: Excellent 🌟")
    print("You are on a strong academic track!")

elif performance_cgpa >= 3.0 and progress >= 50:
    print("Overall Performance: Good 👍")
    print("Keep improving your consistency.")

elif performance_cgpa >= 2.0:
    print("Overall Performance: Average 📚")
    print("Focus more on weak subjects and regular revision.")

else:
    print("Overall Performance: Needs Improvement 💪")
    print("Create a regular study routine and practice daily.")

print("\nPerformance analysis completed successfully! ✅")
# ----- STUDENT DASHBOARD -----

print("\n==============================")
print("       STUDENT DASHBOARD")
print("==============================")

student_name = input("Enter student name: ")
student_semester = input("Enter current semester: ")
student_field = input("Enter field of study: ")

print("\n----- Student Summary -----")
print("Name:", student_name)
print("Semester:", student_semester)
print("Field:", student_field)

print("\n----- Dashboard Status -----")
print("Study Planner: Available ✅")
print("Progress Tracker: Available ✅")
print("CGPA Calculator: Available ✅")
print("Study Recommendation: Available ✅")
print("Performance Analysis: Available ✅")

print("\nStudent dashboard created successfully! 🎓")