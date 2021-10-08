import random


game = True
list = ['green', 'red', 'blue']


answer = input("WHAT WILL THE COLOR BE GREEN, RED, OR BLUE!?????")

num = random.randint(1, 3)

while game:
    if list[num] == answer:
        print("Congrats! You guessed correctly")
        print("SEE YA")
        game = False
    else: 
        print("wrong answer, try again")
        answer = input("WHAT WILL THE COLOR BE GREEN, RED, OR BLUE!?????")
