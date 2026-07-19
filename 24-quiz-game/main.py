
questions = ("1. How many elements  are in the periodic table?: ",
             "2. Which animal lays the largest egg?: ",
             "3. What is the most abundant gas in Earth's atmosphere?: ",
             "4. How many bones are in the human body?: ",
             "5. Which planet in the solar system is the hottest?: ")

options = (("A. 116", "B. 117", "C. 118", "D. 119"),
           ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
           ("A. Nitrogen", "B. Oxygen", "C. Carbon-Dioxide", "D. Hydrogen"),
           ("A. 206", "B. 207", "C. 208", "D. 209"),
           ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"))

answers = ("C", "D", "A", "A", "B")
guesses = []
score = 0
questionNums = 0

for question in questions:
    print("---------------------------------------------")
    print(question)
    for option in options[questionNums]:
        print(option)

    guess = input("Enter the answer (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[questionNums]:
        score += 1
        print("ANSWET CORRECT")
    else:
        print("ANSWER INCORRET")
        print(f"{answers[questionNums]} is the correct answer")
    questionNums += 1

print("---------------------------------------------")
print("                   RESULT                    ")
print("---------------------------------------------")

print("Guesses: ", end=" ")
for gues in guesses:
    print(guess, end=" ")
print()

print("Answer: ", end=" ")
for answer in answers:
    print(answer, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your score is: {score} %")

