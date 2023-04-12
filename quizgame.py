print("Hey, there welcome to the basic quiz game!")
print("This game is an anime quiz, you are going to have fun!")

doYouWantToPlay = input("Are you playing this game?\n")
# print(doYouWantToPlay)
if doYouWantToPlay == "Yes":
    print("Yes I am playing")
else:
    quit()

countOfScore = 0
countOfRightAnswers = 0
countOfWrongAnswrs = 0
countOfTotalQuestions = 0
print("So, let's go, play this amazing quiz\n")

print("Question 1")
print("What is the name of the world's largest ocean?")
print("1. Atlantic\n2. Pacific\n3. Indian\n4. Arctic")
questionOne = input("Write the full answer here: ")
if questionOne == "Pacific":
    print("Yay", questionOne, "is the right answer")
    print("So, you got the first one correct")
    countOfScore += 1

    countOfRightAnswers += 1
else:
    print("Oops, that is a wrong answer")
    countOfScore -= 1

    countOfWrongAnswrs += 1
countOfTotalQuestions += 1
print("Number of right answers you gave:", countOfRightAnswers)
print("Number of wrong answers you gave:", countOfWrongAnswrs)

print("\n")

print("Question 2")
print("What is the capital of Canada?")
print("A. Ottawa\nB. Toronto\nC. Vancouver\nD. Montreal")
questionTwo = input("Write the full answer here: ")
if questionTwo == "Ottawa":
    print("Yay", questionTwo, "is the right answer")
    print("So, you got the second one correct")
    countOfScore += 1

    countOfRightAnswers += 1
else:
    print("Oops, that is a wrong answer")
    countOfScore -= 1

    countOfWrongAnswrs += 1
countOfTotalQuestions += 1
print("Number of right answers you gave:", countOfRightAnswers)
print("Number of wrong answers you gave:", countOfWrongAnswrs)

print("\n")


print("Question 3")
print("Who is the current Chancellor of Germany?")
print("A. Angela Merkel\nB. Frank-Walter Steinmeier\nC. Olaf Scholz\nD. Annalena Baerbock")
questionThree = input("Write the full answer here: ")
if questionThree == "Olaf Scholz":
    print("Yay", questionThree, "is the right answer")
    print("So, you got the third one correct")
    countOfScore += 1

    countOfRightAnswers += 1
else:
    print("Oops, that is a wrong answer")
    countOfScore -= 1

    countOfWrongAnswrs += 1
countOfTotalQuestions += 1
print("Number of right answers you gave:", countOfRightAnswers)
print("Number of wrong answers you gave:", countOfWrongAnswrs)

print("\n")

print("Question 4")
print("Which planet in our solar system is the smallest?")
print("A. Mars\nB. Mercury\nC. Venus\nD. Pluto")
questionFour = input("Write the full answer here: ")
if questionFour == "Mercury":
    print("Yay", questionFour, "is the right answer")
    print("So, you got the forth one correct")
    countOfScore += 1

    countOfRightAnswers += 1
else:
    print("Oops, that is a wrong answer")
    countOfScore -= 1

    countOfWrongAnswrs += 1
countOfTotalQuestions += 1
print("Number of right answers you gave:", countOfRightAnswers)
print("Number of wrong answers you gave:", countOfWrongAnswrs)

print("\n")

print("Question 5")
print("What is the largest landlocked country in the world?")
print("A. Mongolia\nB. Kazakhstan\nC. Afghanistan\nD. Niger")
questionFive = input("Write the full answer here: ")
if questionFive == "Kazakhstan":
    print("Yay", questionFive, "is the right answer")
    print("So, you got the fifth one correct")
    countOfScore += 1

    countOfRightAnswers += 1
else:
    print("Oops, that is a wrong answer")
    countOfScore -= 1

    countOfWrongAnswrs += 1
countOfTotalQuestions += 1
print("Number of right answers you gave:", countOfRightAnswers)
print("Number of wrong answers you gave:", countOfWrongAnswrs)

print("\n")

print("Question 6")
print("Who is the author of the Harry Potter series?")
print("A. Stephen King\nB. J.K. Rowling\nC. Dan Brown\nD. George R.R. Martin")
questionSix = input("Write the full answer here: ")
if questionSix == "J.K. Rowling":
    print("Yay", questionSix, "is the right answer")
    print("So, you got the sixth one correct")
    countOfScore += 1

    countOfRightAnswers += 1
else:
    print("Oops, that is a wrong answer")
    countOfScore -= 1

    countOfWrongAnswrs += 1
countOfTotalQuestions += 1
print("Number of right answers you gave:", countOfRightAnswers)
print("Number of wrong answers you gave:", countOfWrongAnswrs)

print("\n")

print("Question 7")
print("Who is the founder of Amazon.com?")
print("A. Steve Jobs\nB. Jeff Bezos\nC. Mark Zuckerberg\nD. Bill Gates")
questionSeven = input("Write the full answer here: ")
if questionSeven == "Jeff Bezos":
    print("Yay", questionSeven, "is the right answer")
    print("So, you got the seventh one correct")
    countOfScore += 1

    countOfRightAnswers += 1
else:
    print("Oops, that is a wrong answer")
    countOfScore -= 1

    countOfWrongAnswrs += 1
countOfTotalQuestions += 1
print("Number of right answers you gave:", countOfRightAnswers)
print("Number of wrong answers you gave:", countOfWrongAnswrs)

print("\n")

print("Question 8")
print("Who is the current President of the United States?")
print("A. Joe Biden\nB. Donald Trump\nC. Barack Obama\nD. George W. Bush")
questionEight = input("Write the full answer here: ")
if questionEight == "Joe Biden":
    print("Yay", questionEight, "is the right answer")
    print("So, you got the eighth one correct")
    countOfScore += 1

    countOfRightAnswers += 1
else:
    print("Oops, that is a wrong answer")
    countOfScore -= 1

    countOfWrongAnswrs += 1
countOfTotalQuestions += 1
print("Number of right answers you gave:", countOfRightAnswers)
print("Number of wrong answers you gave:", countOfWrongAnswrs)

print("\n")

print("Question 9")
print("What is the highest mountain in Africa?")
print("A. Mount Everest\nB. Kilimanjaro\nC. Mount Fuji\nD. Mount Kilahuea")
questionNine = input("Write the full answer here: ")
if questionNine == "Kilimanjaro":
    print("Yay", questionNine, "is the right answer")
    print("So, you got the ninth one correct")
    countOfScore += 1

    countOfRightAnswers += 1
else:
    print("Oops, that is a wrong answer")
    countOfScore -= 1

    countOfWrongAnswrs += 1
countOfTotalQuestions += 1
print("Number of right answers you gave:", countOfRightAnswers)
print("Number of wrong answers you gave:", countOfWrongAnswrs)

print("\n")

print("Question 10")
print("Which country won FIFA WC 2022?")
print("A. Portugal\nB. Netherlands\nC. Brazil\nD. Argentina")
questionTen = input("Write the full answer here: ")
if questionTen == "Argentina":
    print("Yay", questionTen, "is the right answer")
    print("So, you got the nineth one correct")
    countOfScore += 1

    countOfRightAnswers += 1
else:
    print("Oops, that is a wrong answer")
    countOfScore -= 1

    countOfWrongAnswrs += 1
countOfTotalQuestions += 1
print("Number of right answers you gave:", countOfRightAnswers)
print("Number of wrong answers you gave:", countOfWrongAnswrs)

print("\n")

print("Complete list of right answers\n")
print("1. Pacific\n2. Ottawa\n3. Olaf Scholz\n4. Mercury\n5. Kazakhstan\n6. J.K. Rowling\n7. Jeff Bezos\n8. Joe Biden\n9. Kilimanjaro\n10. Argentina\n")

print("You have finished the quiz, congratulations")
print("And now, it is time for your quiz scores")
print("You scored", countOfScore, "points")
print("Percentage of right answers: ",
      (countOfRightAnswers/countOfTotalQuestions) * 100, "%")
print("Percentage of wrong answers: ",
      (countOfWrongAnswrs/countOfTotalQuestions) * 100, "%")


print("So, thank you for playing this quiz, see you soon again!")
