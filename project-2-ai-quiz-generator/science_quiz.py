def science_quiz():
    questions = [
        {
            "question": "1. Which planet is known as the Red Planet?",
            "options": ["A. Earth", "B. Venus", "C. Mars", "D. Jupiter"],
            "answer": "C"
        },
        {
            "question": "2. What is the chemical symbol for water?",
            "options": ["A. O2", "B. CO2", "C. H2O", "D. HO"],
            "answer": "C"
        },
        {
            "question": "3. Which gas do plants absorb from the atmosphere?",
            "options": ["A. Oxygen", "B. Nitrogen", "C. Carbon Dioxide", "D. Hydrogen"],
            "answer": "C"
        },
        {
            "question": "4. What is the largest organ in the human body?",
            "options": ["A. Heart", "B. Brain", "C. Skin", "D. Liver"],
            "answer": "C"
        },
        {
            "question": "5. What force pulls objects toward the Earth?",
            "options": ["A. Friction", "B. Gravity", "C. Magnetism", "D. Energy"],
            "answer": "B"
        },
        {
            "question": "6. Which part of the plant makes food?",
            "options": ["A. Root", "B. Stem", "C. Leaf", "D. Flower"],
            "answer": "C"
        },
        {
            "question": "7. Which planet is the largest in our Solar System?",
            "options": ["A. Earth", "B. Saturn", "C. Jupiter", "D. Neptune"],
            "answer": "C"
        },
        {
            "question": "8. Which vitamin is produced by sunlight?",
            "options": ["A. Vitamin A", "B. Vitamin B", "C. Vitamin C", "D. Vitamin D"],
            "answer": "D"
        },
        {
            "question": "9. How many bones are there in an adult human body?",
            "options": ["A. 198", "B. 206", "C. 212", "D. 220"],
            "answer": "B"
        },
        {
            "question": "10. Which gas is essential for human breathing?",
            "options": ["A. Carbon Dioxide", "B. Nitrogen", "C. Oxygen", "D. Helium"],
            "answer": "C"
        }
    ]

    score = 0

    print("\n========== Science Quiz ==========\n")

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
        message = "🌟 Outstanding! You have excellent Science knowledge!"
    elif percentage >= 80:
        grade = "A"
        message = "🎉 Excellent Work!"
    elif percentage >= 70:
        grade = "B"
        message = "👏 Very Good!"
    elif percentage >= 60:
        grade = "C"
        message = "🙂 Good Job! Keep Learning."
    elif percentage >= 50:
        grade = "D"
        message = "📚 You Passed. Practice More."
    else:
        grade = "F"
        message = "💪 Never Give Up. Try Again!"

    print(f"Grade           : {grade}")
    print(message)

    print("=" * 40)
    input("Press Enter to return to Main Menu...")