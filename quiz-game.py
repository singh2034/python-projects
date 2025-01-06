# Let's make a quiz game
print("Welcome to my computer quiz!")

# let's ask the user
playing = str(input("Do you want to play?\n"))

# check if user wants to play?
if playing.lower() == "yes" :
    print("Ok! Let's play :)")
    print("You will get 1 score for each correct answer and -1 score for incorrect answer.")
else :
    playing.lower() == "no" 
    print("Ok, see you next time.")
    # inbuilt python function
    quit()


# count score
score = 0


# let's ask a question
# question 1
print("Here is the question 1")
answer = str(input("What does CPU stands for?\n"))

# validation for correct answer
if answer.lower() == "central processing unit" :
    print("Correct!")
    score += 1
    print("Your score is: ", score)
else :
    print("Incorrect!")
    score -= 1
    print("Your score is: ", score)

# question 2
print("Here is the question 2")
answer = str(input("What does GPU stands for?\n"))

# validation for correct answer
if answer.lower() == "graphics processing unit" :
    print("Correct!")
    score += 1
    print("Your score is: ", score)
else :
    print("Incorrect!")
    score -= 1
    print("Your score is: ", score)

# question 3
print("Here is the question 3")
answer = str(input("What does RAM stands for?\n"))

# validation for correct answer
if answer.lower() == "random access memory" :
    print("Correct!")
    score += 1
    print("Your score is: ", score)
else :
    print("Incorrect!")
    score -= 1
    print("Your score is: ", score)

# question 4
print("Here is the question 4")
answer = str(input("What does ROM stands for?\n"))

# validation for correct answer
if answer.lower() == "read only memory" :
    print("Correct!")
    score += 1
    print("Your score is: ", score)
else :
    print("Incorrect!")
    score -= 1
    print("Your score is: ", score)

# question 5
print("Here is the question 5")
answer = str(input("What does HDD stands for?\n"))

# validation for correct answer
if answer.lower() == "hard disk drive" :
    print("Correct!")
    score += 1
    print("Your score is: ", score)
else :
    print("Incorrect!")
    score -= 1
    print("Your score is: ", score)

# quetion 6
print("Here is the question 6")
answer = str(input("What does SSD stands for?\n"))

# validation for correct answer
if answer.lower() == "solid state drive" :
    print("Correct!")
    score += 1 
    print("Your score is: ", score)
else :
    print("Incorrect!")
    score -= 1
    print("Your score is: ", score)

# result
print("Your Total score is = ", score)
print("Your percentage is = ", round((score/6) * 100))