def math_quiz():
    questions = [
        {
            "question": "1. What is the value of 12 × 8?",
            "options": ["A. 84", "B. 96", "C. 108", "D. 88"],
            "answer": "B"
        },
        {
            "question": "2. What is the square root of 144?",
            "options": ["A. 10", "B. 11", "C. 12", "D. 14"],
            "answer": "C"
        },
        {
            "question": "3. Solve: 15 + 27 = ?",
            "options": ["A. 40", "B. 41", "C. 42", "D. 43"],
            "answer": "C"
        },
        {
            "question": "4. What is 9²?",
            "options": ["A. 72", "B. 81", "C. 90", "D. 99"],
            "answer": "B"
        },
        {
            "question": "5. Which number is prime?",
            "options": ["A. 15", "B. 18", "C. 19", "D. 21"],
            "answer": "C"
        },
        {
            "question": "6. What is 100 ÷ 4?",
            "options": ["A. 20", "B. 25", "C. 30", "D. 35"],
            "answer": "B"
        },
        {
            "question": "7. Value of π is approximately?",
            "options": ["A. 2.14", "B. 3.14", "C. 4.13", "D. 3.41"],
            "answer": "B"
        },
        {
            "question": "8. What is 7 × 9?",
            "options": ["A. 56", "B. 63", "C. 72", "D. 69"],
            "answer": "B"
        },
        {
            "question": "9. Solve: 45 − 19 = ?",
            "options": ["A. 24", "B. 25", "C. 26", "D. 27"],
            "answer": "C"
        },
        {
            "question": "10. Which is an even number?",
            "options": ["A. 17", "B. 19", "C. 22", "D. 25"],
            "answer": "C"
        }
    ]

    score = 0

    print("\n========== Mathematics Quiz ==========\n")

    for q in questions:
        print(q["question"])

        for option in q["options"]:
            print(option)

        user = input("Your Answer (A/B/C/D): ").upper()

        if user == q["answer"]:
            print("✅ Correct!\n")
            score += 1
        else:
            print(f"❌ Wrong! Correct Answer: {q['answer']}\n")
            print("=" * 40)
    print("Quiz Completed!")
    print("=" * 40)

    print(f"Your Score      : {score}/{len(questions)}")

    percentage = (score / len(questions)) * 100
    print(f"Percentage      : {percentage:.1f}%")

    if percentage >= 90:
        grade = "A+"
        message = "🌟 Outstanding! You are a Math Champion!"
    elif percentage >= 80:
        grade = "A"
        message = "🎉 Excellent Work!"
    elif percentage >= 70:
        grade = "B"
        message = "👏 Very Good!"
    elif percentage >= 60:
        grade = "C"
        message = "🙂 Good Job! Keep Practicing."
    elif percentage >= 50:
        grade = "D"
        message = "📚 You Passed. Practice More."
    else:
        grade = "F"
        message = "💪 Don't Give Up. Try Again!"

    print(f"Grade           : {grade}")
    print(message)

    print("=" * 40)
    input("Press Enter to return to Main Menu...")