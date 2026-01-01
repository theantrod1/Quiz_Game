print("Welcome to my game!")
playing = input("Do you want to play? (yes/no) ")
if playing.lower() != "yes":
    print("alright then")
    quit()
else:
    print("Let's play!")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("correct!")
    score += 1
else:
    print("incorrect")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("correct!")
    score += 1
else:
    print("incorrect")

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("correct!")
    score += 1
else:
    print("incorrect")

if score > 1:
    print(f"You got {score} questions correct!")
else:
    print(f"You got {score} question correct!")
print(f"Your final score is {score / 3 * 100}%")
