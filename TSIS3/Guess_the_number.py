import random
rand = random.randrange(1, 20)
print("Hello! What is your name?")
name = input()

print(f"Well, {name}, I am thinking of a number between 1 and 20.")
print("Take a guess.")

cnt = 0
while True:
    num = int(input())
    cnt += 1
    if num == rand:
        print(f"Good job, {name}! You guessed my number in {cnt} guesses!")
        break
    else:
        if rand > num:
            print("Your guess is too low.")
            print("Take a guess.")
        else: 
            print("Your guess is too big.")
            print("Take a guess.")