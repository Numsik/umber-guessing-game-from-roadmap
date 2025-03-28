import random


def main():
    mode = input("What mode you want (easy/medium/hard): ").lower()

    if mode == "easy":
        easy()
    elif mode == "medium":
        medium()
    else:
        hard()


def easy():
    easy_random = random.randint(1, 5)
    attempts = 0
    max_attempts = 3

    while attempts < max_attempts:
        your_tip = int(input("Enter a number 1-5: "))
        if your_tip == easy_random:
            print("Correct!")
            return
        else:
            attempts += 1
            print("Wrong! Attempts left:", max_attempts - attempts)

    print("You lost! The number was:", easy_random)


def medium():
    medium_random = random.randint(1, 15)
    attempts = 0
    max_attempts = 5

    while attempts < max_attempts:
        your_tip = int(input("Enter a number 1-15: "))
        if your_tip == medium_random:
            print("Correct!")
            return
        else:
            attempts += 1
            print("Wrong! Attempts left:", max_attempts - attempts)

    print("You lost! The number was:", medium_random)


def hard():
    hard_random = random.randint(1, 50)
    attempts = 0
    max_attempts = 7

    while attempts < max_attempts:
        your_tip = int(input("Enter a number 1-50: "))
        if your_tip == hard_random:
            print("Correct!")
            return
        else:
            attempts += 1
            print("Wrong! Attempts left:", max_attempts - attempts)

    print("You lost! The number was:", hard_random)


if __name__ == '__main__':
    main()
