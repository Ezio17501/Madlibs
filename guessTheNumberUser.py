import random
def computer_guess(x):
    low = 1
    high = x
    feedback = ""
    while feedback != "c":
        if low == high:
            guess = 1
        else:
            guess = random.randint(low,high)
        feedback = input(f"{guess} too high (H), too low (L), or correct (C)??").lower()
        if feedback == "h":
            high = guess-1
        elif feedback == "l":
            low = guess+1

    print(f"yay! The computer guessed your number, {guess}, correctly!")

computer_guess(1000)