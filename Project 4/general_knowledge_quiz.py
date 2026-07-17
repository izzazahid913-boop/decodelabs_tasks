# =============================================================
# DecodeLabs Internship
# Python Programming Project 4
#
# Project Name : General Knowledge Quiz
# Developed By : Izza Zahid
#
# Description:
# This program asks General Knowledge questions,
# checks user answers,
# calculates the score,
# and displays the final result.
# =============================================================

print("=" * 60)
print("      WELCOME TO THE GENERAL KNOWLEDGE QUIZ")
print("=" * 60)
print("Instructions:")
print("1. There are 3 questions.")
print("2. Each correct answer gives you 1 point.")
print("3. Type your answer carefully.")
print("=" * 60)

# Score Variable
score = 0
# ------------------------------
# Question 1
# ------------------------------

print("\nQuestion 1")
print("What is the capital of Pakistan?")

answer = input("Your Answer: ")

if answer.lower() == "islamabad":
    print("✅ Correct!")
    score += 1

else:
    print("❌ Wrong!")
    print("Correct Answer: Islamabad")

    # ------------------------------
# Question 2
# ------------------------------

print("\nQuestion 2")
print("How many continents are there in the world?")

answer = input("Your Answer: ")

if answer == "7":
    print("✅ Correct!")
    score += 1

else:
    print("❌ Wrong!")
    print("Correct Answer: 7")

    # ------------------------------
# Question 3
# ------------------------------

print("\nQuestion 3")
print("Which planet is known as the Red Planet?")

answer = input("Your Answer: ")

if answer.lower() == "mars":
    print("✅ Correct!")
    score += 1

else:
    print("❌ Wrong!")
    print("Correct Answer: Mars")

    # ------------------------------
# Final Result
# ------------------------------

print("\n" + "=" * 60)
print("              QUIZ COMPLETED")
print("=" * 60)

print(f"Your Final Score: {score}/3")

if score == 3:
    print("🏆 Excellent! Outstanding Performance!")

elif score == 2:
    print("👏 Very Good! Keep Learning.")

elif score == 1:
    print("🙂 Good Attempt! Practice More.")

else:
    print("😔 Better Luck Next Time!")

print("=" * 60)
print("Thank you for playing the quiz!")
print("=" * 60)