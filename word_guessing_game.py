import random

name=input("Enter your Name: ")
print("Good Luck ",name)
words = ['rainbow', 'computer', 'science', 'programming','python', 'mathematics', 'player', 'condition','reverse', 'water', 'board', 'geeks']
print("Guess from this words",words)
b=random.choice(words)
score=0
#print(b)   to know the guessing word
for i in range(0,5):
    guess=input("Guess the word: ")
    if guess in b:
        print("You WIN")
        score+=5
        break
    else:
        if i==4:
            print("You LOOSE")
            score-=1
        else:
            print("WRONG")
            score-=1
print(name,"your score is ",score)