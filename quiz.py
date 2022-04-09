from components.quizQuestions import questions
from components import quizVars, quizPoints
from colorama import Fore, Back

print(Fore.WHITE + "WELCOME TO A MARVEL CHARACTERS SCRIPT GAME!")
print(Fore.WHITE + "============================================")
print(Fore.WHITE + "Choose between the following characters, and I'll try to guess who you picked!")
print(Back.GREEN + "========== HULK ==========")
print(Back.YELLOW + "========== THOR ==========")
print(Back.RED + "========== BLACK WIDOW ==========")
print(Back.BLUE + "========== CAPTAIN AMERICA ==========")
print(Back.RED + "========== WANDA ==========")
print(Back.YELLOW + "========== IRON MAN ==========")
print(Back.GREEN + "========== LOKI ==========")

print(Back.BLACK + "===========================================")
print(Fore.WHITE + "Let's begin!")

answer1 = questions["q1"][input(questions["q1"]["question"])]
print(answer1)

quizVars.quizTotal += answer1
print(">>>>>>>>>>>>>>>>>>>>\n")

answer2 = questions["q2"][input(questions["q2"]["question"])]
print(answer2)

quizVars.quizTotal += answer2
print(">>>>>>>>>>>>>>>>>>>>\n")

answer2 = questions["q3"][input(questions["q3"]["question"])]
print(answer2)

quizVars.quizTotal += answer2
print(">>>>>>>>>>>>>>>>>>>>\n")

answer2 = questions["q4"][input(questions["q4"]["question"])]
print(answer2)

quizVars.quizTotal += answer2
print(">>>>>>>>>>>>>>>>>>>>\n")

answer2 = questions["q5"][input(questions["q5"]["question"])]
print(answer2)

quizVars.quizTotal += answer2
print(">>>>>>>>>>>>>>>>>>>>\n")

answer2 = questions["q6"][input(questions["q6"]["question"])]
print(answer2)

quizVars.quizTotal += answer2
print(">>>>>>>>>>>>>>>>>>>>\n")

answer2 = questions["q7"][input(questions["q7"]["question"])]
print(answer2)

quizVars.quizTotal += answer2
print(">>>>>>>>>>>>>>>>>>>>\n")


print("total so far: " + str(quizVars.quizTotal) + "\n")

quizPoints.total(quizVars.quizTotal)
