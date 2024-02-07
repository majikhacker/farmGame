import random

def game_intro():
    print("Hello!")
    user_name = input("What's your name? ")
    print(f"Nice to meet you, {user_name}!")

def get_animal_choice():
    print("Let's play Safari-Nanegans! What's your favorite animal?:")
    print("1. Dog") 
    print("2. Cat")
    print("3. Duck")
    print("4. Cow")
    print("5. Sheep")
    print("6. Elephant")
    print("7. Lion")
    print("8. Frog")
    print("9. Monkey")
    print("10. Tio Bear")
    print("11. Exit game")

    choice = input("Enter the number of the animal you want to hear: ")
    print()
    print("Good choice! That animal sounds like this....",) 
    print()
    return choice
    print()
    print("Ok, pick another animal and let's hear what it sounds like!")    

def play_animal_sound(animal):
    sounds = {
        "1": "Woof woof!",
        "2": "Meow meow!",
        "3": "Quack quack!",
        "4": "Moo moo!",
        "5": "Baa baa!",
        "6": "Trumpet sound!",
        "7": "Roarrr!",
        "8": "Ribbit ribbit!",
        "9": "Ooh ooh ah ah!",
        "10": "Blippity bloppity boo!", 
    }
    sound = sounds.get(animal, "Sorry, I don't know that animal.")
    print(f"{sound}")

def main():
    game_intro()

    while True:
        choice = get_animal_choice()

        if choice == "11":
            print("Thanks for playing! Goodbye!")
            break

        play_animal_sound(choice)

if __name__ == "__main__":
    main()