
from random import randint

limit = 0
print("Welcome to the guessing game !")
print("I am thinking of a game between 1 and 100")
answer = randint(1, 100)


counter = 0
checker=0


def check_answer(guess, answer):
    if guess > answer:
        print("Too High")
    elif guess < answer:
        print("Too Low")
    else:
        global checker
        print("You go the correct answer !")
        checker=1


def choose_difficulty():
    w = input("Please choose difficulty easy or hard 'e' or 'h': ")
    global counter
    if w == 'e':
        counter = 10
    else:
        counter = 5


choose_difficulty()

i = 0
while i != counter:
    guess = int(input("Please guess a number:"))
    check_answer(guess,answer)
    if checker ==1:
        print("you have won !")
        break
    i += 1
    if i == counter:
        print('YOU HAVE LOST SADLY !')
        break
