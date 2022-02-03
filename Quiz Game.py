game = input("Do you want to play game---yes/no : ")

if game.lower() != "yes":
    quit("ok")
score = 0
print("lets play the game :)\n")
# question 1
answer = input("Are list mutable?: ")
if answer.lower() == "yes":
    print("correct")
    score += 1
else:
    print("incorrect")

# question 2
answer = input("Are tuples mutable?: ")
if answer.lower() == "no":
    print("correct")
    score += 1
else:
    print("incorrect")

# question 3
answer = input("What is the full form of RDBMS?: ")
if answer.lower() == "relational database management system":
    print("correct")
    score += 1
else:
    print("incorrect")

print("\nyou got " + str(score) + ' question correct')
if score == 3:
    print("WOW! all your answers are correct")
else:
    print("Thank you! Good Luck")
