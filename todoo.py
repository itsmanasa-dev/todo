# Simple Python Quiz App

def quiz():
    questions = {
        "1. What is the capital of France?": "b",
        "2. Which language is used for web apps?": "a",
        "3. Who developed Python?": "c",
        "4. What is 7 * 8?": "d",
        "5. What keyword is used to define a function in Python?": "b"
    }

    options = [
        ["a. Java", "b. Python", "c. HTML", "d. C++"],
        ["a. JavaScript", "b. SQL", "c. Photoshop", "d. MS Word"],
        ["a. Bill Gates", "b. Elon Musk", "c. Guido van Rossum", "d. Mark Zuckerberg"],
        ["a. 54", "b. 58", "c. 60", "d. 56"],
        ["a. func", "b. def", "c. function", "d. define"]
    ]

    score = 0
    print("\n✨ Welcome to the Python Quiz Game ✨")
    print("-----------------------------------")

    for i, (question, answer) in enumerate(questions.items()):
        print(f"\n{question}")
        for opt in options[i]:
            print(opt)
        user_answer = input("Enter your answer (a/b/c/d): ").lower()

        if user_answer == answer:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong! Correct answer is '{answer}'.")

    print("\n-----------------------------------")
    print(f"🎯 Your final score: {score}/{len(questions)}")
    if score == len(questions):
        print("🏆 Excellent! You’re a genius!")
    elif score >= 3:
        print("👍 Good job! Keep practicing.")
    else:
        print("😅 You need to study more!")

# Run the quiz
quiz()
