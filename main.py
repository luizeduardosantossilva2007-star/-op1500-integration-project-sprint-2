#student name: Luiz Eduardo Santos Silva
#this program is a simples quiz with 5 questions with 3 levels of difficulty and each level is worth a different amount of points. this programs also has a score counter system


print("hello, this is a game quiz about the japanese animation Neon Genesis Evangelion", end="! ")

print("the rules are very simple!")
print("rule number 1 - the quiz is 5 questions long")
print("rule number 2 - the questions vary in difficulty. Harder questions are worth more points")
print("rule number 3 - if you never watched the series feel free to search in the internet about it to help you")

questionResults = []

score = 0



easyWeight = 1 #weight for each difficulty level
mediumWeight = 3
hardWeight = 5



print("question number 1 (difficulty: easy) - whats the name of the protagonist of the series?") #question

option_A_question1 = "Shinji Ikari" #the option that will be printed below
option_B_question1 = "Misato Katsuragi"
option_C_question1 = "Gendo Ikari"
option_D_question1 = "Asuka Soryu"

print(option_A_question1)
print(option_B_question1)
print(option_C_question1)
print(option_D_question1)

attemptq1 = 0 #inital number of attemps per question

while attemptq1 <= 2: #loop to count the attempts and to check if the answer is correct, wrong or simply not an option
    answerq1 = input("select a option:")
    if answerq1 == "A" or answerq1 == "a":
        print("you are right")
        question1score = 1
        break
    elif answerq1 == "B" or answerq1 == "b" or answerq1 == "C" or answerq1 == "c" or answerq1 == "D" or answerq1 == "d":
        print("you are wrong")
        attemptq1 += 1
    elif answerq1 != ("A", "B", "C", "D", "a", "b", "c", "d"):
        print("not an option")
        attemptq1 += 1

questionResults.append((question1score , easyWeight))

print("question number 2 (difficulty easy) - whats the name of the evangelion that appears in the first episode?")

option_A_question2 = "Rx 78-2"
option_B_question2 = "Eva unit 13"
option_C_question2 = "Jet Alone"
option_D_question2 = "Eva unit 01"

print(option_A_question2)
print(option_B_question2)
print(option_C_question2)
print(option_D_question2)

attemptq2 = 0

while attemptq2 <= 2:
    answerq2 = input("select a option:")
    if answerq2 == "D" or answerq2 == "d":
        print("you are right")
        question2score = 1
        break
    elif answerq2 == "A" or answerq2 == "a" or answerq2 == "B" or answerq2 == "b" or answerq2 == "C" or answerq2 == "c":
        print("you are wrong")
        attemptq2 += 1
    elif answerq2 != ("A", "B", "C", "D", "a", "b", "c", "d"):
        print("not an option")
        attemptq2 += 1

questionResults.append((question2score, easyWeight))

print("question number 3 (difficulty easy) - did Shinji initially wanted to pilot the Eva?")

option_A_question3 = "Yes"
option_B_question3 = "No"

print(option_A_question3)
print(option_B_question3)

attemptq3 = 0

while attemptq3 <= 2:
    answerq3 = input("select a option:")
    if answerq3 == "B" or answerq3 == "b":
        print("you are right")
        question3score = 1
        break
    elif answerq3 == ("A", "B"):
        print("you are wrong")
        attemptq3 += 1
    elif answerq3 != ("A", "B", "a", "b"):
        print("not an option")
        attemptq3 += 1

questionResults.append((question3score, easyWeight))

print("question number four (difficulty medium) - what the Evas really are?")

option_A_question4 = "Gigant Robots"
option_B_question4 = "Aliens"
option_C_question4 = "Clones from Adam and Lilith"
option_D_question4 = "AI"

print(option_A_question4)
print(option_B_question4)
print(option_C_question4)
print(option_D_question4)

attemptq4 = 0

while attemptq4 <= 2:
    answerq4 = input("select a option:")
    if answerq4 == "C" or answerq4 == "c":
        print("you are right")
        question4score = 3
        break
    elif answerq4 == "A" or answerq4 == "a" or answerq4 == "B" or answerq4 == "b" or answerq4 == "D" or answerq4 == "d":
        print("you are wrong")
        attemptq4 += 1
    elif answerq4 != ("A", "B", "C", "D", "a", "b", "c", "d"):
        print("not an option")
        attemptq4 += 1

questionResults.append((question4score, mediumWeight))

print("question number five (difficulty hard) - what was Gendo Ikari (Shinji's father) real plan in the end?")

option_A_question5 = "Option A: Use the human instrumentality project to reunite with his wife"
option_B_question5 = "Option B: use the human instrumentality to control the world"
option_C_question5 = "Option C: Use the human instrumentality to destroy the world"
option_D_question5 = "Option D: Utilize the power of the impact to rebuilde the world in his image"

print(option_A_question5)
print(option_B_question5)
print(option_C_question5)
print(option_D_question5)

attemptq5 = 0

while attemptq5 <= 2:
    answerq5 = input("select a option:")
    if answerq5 == "A" or answerq5 == "a":
        print("you are right")
        question5score = 5
        break
    elif answerq5 == "B" or answerq5 == "b" or answerq5 == "c" or answerq5 == "c" or answerq5 == "d" or answerq5 == "d":
        print("you are wrong")
        attemptq5 += 1
    elif answerq5 != ("A", "B", "C", "D", "a", "b", "c", "d"):
        print("not an option")
        attemptq5 += 1

questionResults.append((question5score, hardWeight))

def calculateScore (result):
    totalscore = 0
    totalweight = 0

    for score, weight in result:
        totalscore += score * weight
        totalweight += weight

    if totalweight == 0:
        return 0
    else:
        finalscore = totalscore / totalweight
        return finalscore

finalscore = calculateScore(questionResults)

print(f"your final score is {finalscore:.2f}")







    #took out the numeric operator demostration because it was on the last sprint so i believe its unecessary to show it again, same to the string operators demo
