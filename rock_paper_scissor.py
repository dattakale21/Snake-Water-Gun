import random


def rock_paper_siccor(computer, you):
    if computer == you:
        return None

    elif computer == 'r':
        if you == 'p':
            return True
        elif you == 's':
            return False

    elif computer == 'p':
        if you == 'r':
            return False
        elif you == 's':
            return True

    elif computer == 's':
        if you == 'p':
            return False
        elif you == 'r':
            return True


print("Computer's choice: ")
ran = random.randint(1, 3)
if ran == 1:
    compter = 'r'
elif ran == 2:
    computer = 'p'
else:
    computer = 's'

you = input("Enter your choice: ")
print("\r")
print("\r")
a = rock_paper_siccor(computer, you)
print("computer's choice: ", computer)
print("your's choice: ", you)
print("\r")
print("\r")
if a == None:
    print("The game is tie!")
elif a:
    print("********** You win! ***********")
else:
    print("********** You lose! ***********")
