def english_quiz():
    questions = [
        {
            "question": "1. Choose the correct spelling.",
            "options": ["A. Enviroment", "B. Environment", "C. Environmant", "D. Envirenment"],
            "answer": "B"
        },
        {
            "question": "2. What is the synonym of 'Happy'?",
            "options": ["A. Sad", "B. Angry", "C. Joyful", "D. Weak"],
            "answer": "C"
        },
        {
            "question": "3. Choose the correct sentence.",
            "options": [
                "A. She go to school.",
                "B. She goes to school.",
                "C. She going school.",
                "D. She gone school."
            ],
            "answer": "B"
        },
        {
            "question": "4. What is the opposite of 'Hot'?",
            "options": ["A. Warm", "B. Cold", "C. Heat", "D. Fire"],
            "answer": "B"
        },
        {
            "question": "5. Which word is a noun?",
            "options": ["A. Beautiful", "B. Quickly", "C. Teacher", "D. Run"],
            "answer": "C"
        },
        {
            "question": "6. Fill in the blank: I ___ a student.",
            "options": ["A. is", "B. are", "C. am", "D. be"],
            "answer": "C"
        },
        {
            "question": "7. Which punctuation ends a question?",
            "options": ["A. .", "B. ,", "C. ?", "D. !"],
            "answer": "C"
        },
        {
            "question": "8. Choose the correct article: ___ apple",
            "options": ["A. A", "B. An", "C. The", "D. No article"],
            "answer": "B"
        },
        {
            "question": "9. What is the past tense of 'Go'?",
            "options": ["A. Goed", "B. Gone", "C. Went", "D. Going"],
            "answer": "C"
        },
        {
            "question": "10. Which word is a verb?",
            "options": ["A. Book", "B. Chair", "C. Write", "D. Table"],
            "answer": "C"
        }
    ]

    score = 0

    print("\n========== English Quiz ==========\n")

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
        message = "🌟 Outstanding! Your English is Excellent!"
    elif percentage >= 80:
        grade = "A"
        message = "🎉 Excellent Work!"
    elif percentage >= 70:
        grade = "B"
        message = "👏 Very Good!"
    elif percentage >= 60:
        grade = "C"
        message = "🙂 Good Job! Keep Improving."
    elif percentage >= 50:
        grade = "D"
        message = "📚 You Passed. Practice More."
    else:
        grade = "F"
        message = "💪 Don't Give Up. Keep Learning!"

    print(f"Grade           : {grade}")
    print(message)

    print("=" * 40)
    input("Press Enter to return to Main Menu...")