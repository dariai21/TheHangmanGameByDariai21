import random

def select_a_word(words):
    return random.choice(words)

def first_step(first, second):
    for i in range(len(first)):
        second.append("_")
    for ind in range(len(first)):
        if first[ind] == first_letter:
            second.insert(ind, first_letter)
            second.pop(ind + 1)
        else:
            pass
    return f"Lets begin: {''.join(lower_case)}"

name = input("name: ")
play = input("Click [Enter] to play")

if play == '':
    running = True

else:
    raise SystemExit('Invalid Input. Try again...')


allWords = [
    "elephant", "giraffe", "iguana", "jaguar", "kangaroo", "leopard", "monkey", "octopus", "penguin", "umbrella",
    "vulture", "walrus", "zebra", "bottle", "chair", "desk", "jellyfish", "llama", "newspaper", "toucan",
    "crocodile", "dragonfly", "flamingo", "giraffe", "hedgehog", "insect", "koala", "lizard", "ostrich", "panda",
    "rhinoceros", "scorpion", "tortoise", "whale", "zeppelin", "armadillo", "butterfly", "caterpillar", "dolphin",
    "elephant","firefly", "grasshopper", "hummingbird", "kangaroo", "mantis", "acrobatic", "octopus", "porcupine",
    "quokka", "raccoon", "squirrel", "tarantula", "vampire", "walrus", "magnificent", "yak", "zebra", "alpaca", "bison",
    "chameleon", "dingo", "falcon", "gazelle", "blueberry", "papaya", "lagoon", "apricot", "lemur", "mongoose", "narwhal",
    "ocelot", "panther", "underpass", "rattlesnake", "salamander", "quartz", "fascinating", "vole", "wolverine",
    "highlands", "starfruit", "tangerine", "albatross", "bobcat", "chinchilla", "sensational","hamster", "kiwi",
    "purple", "opossum", "platypus", "raven", "sloth", "tiger", "unicorn", "violet", "wolf", "xylophone", "yacht",
    "angry", "beautiful", "curious", "delicate", "elegant", "fierce", "graceful", "happy", "intelligent",
    "jolly", "kind", "lively", "mysterious", "noisy", "optimistic", "proud", "quick", "radiant", "shy", "timid",
    "unique", "vivid", "witty", "generous", "young", "jealous", "apple", "banana", "carrot", "donut", "eggplant",
    "fries", "grape", "hamburger", "ice cream", "juice", "kiwi", "lemon", "mango", "noodles", "orange", "pizza",
    "quiche", "rice", "strawberry", "tea", "umbrella drink", "vanilla", "watermelon", "school", "yogurt", "zucchini",
    "theatre", "beach", "cave", "desert", "enchanted forest", "farm", "garden", "hill", "island", "jungle", "kitchen",
    "lake", "mountain", "nightclub", "ocean", "park", "village", "river", "seaside", "tavern", "university", "valley",
    "waterfall", "violin", "yacht club", "yellow"
]
while running:
    selected_word = list(select_a_word(allWords))
    lower_case = []
    first_letter = selected_word[0]
    wrong_guesses = 0
    print(first_step(selected_word, lower_case))

    while wrong_guesses != 6:
        if lower_case == selected_word:
            print("Congratulations, you beat me :(")
            play_again = input("Do you want to play again? (y/n)")
            if play_again == 'y':
                break
            elif play_again == 'n':
                print(f"See you again soon {name}!")
                running = False
                break
            else:
                raise SystemExit('Invalid Input. Try again...')

        guess = input("What's your guess?").lower()
        if guess.isalpha() and len(guess) == 1:
            if guess in selected_word:
                for index in range(len(selected_word)):
                    if selected_word[index] == guess:
                        lower_case.insert(index, guess)
                        lower_case.pop(index + 1)
                print(f"That's correct: {''.join(lower_case)}")
            elif guess not in selected_word:
                wrong_guesses += 1
                if wrong_guesses == 1:
                    print("Here comes the head of the hangman!\nYou have 5 more tries")
                elif wrong_guesses == 2:
                    print("Here comes his spine!\nYou have 4 more tries")
                elif wrong_guesses == 3:
                    print("Look, his left arm!\nYou have 3 more tries")
                elif wrong_guesses == 4:
                    print("Look, his right arm!\nYou have 2 more tries")
                elif wrong_guesses == 5:
                    print("Just drew his left leg.\nYou have 1 more try")
                elif wrong_guesses == 6:
                    print("The hangman is complete. I win, you loose!")
                    print(f"The word was {''.join(selected_word)}")
                    play_again = input("Do you want to play again? (y/n)")
                    if play_again == 'y':
                        break
                    elif play_again == 'n':
                        print(f"See you again soon {name}!")
                        running = False
                        break
                    else:
                        raise SystemExit('Invalid Input. Try again...')
        else:
            raise SystemExit('Invalid Input. Try again...')