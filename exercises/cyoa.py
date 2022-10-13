"""EX06 Choose Your Own Adventure: College Pet Life. """

__author__ = "730569341"

import random

"""Assigning global variables."""
    # keep track of your pet's health
points: int = 0 
player: str = []
health: int = 100

# emojis 
SMILE_FACE: str = "U+1F603"
BLUE_HEART: str = "U+1F499"
HUNDRED_EMOJI: str = "U+1F4AF"
EXCLAIMATION: str = "U+203C"
PLEAD_FACE: str = "U+1F97A"
PARTY_POP: str = "U+1F389"

def main() -> None:
    """Entry point of game."""
    greet()
    menu()


def greet() -> None:
    """Welcome message and instructions."""
    print("----------------------------")
    print(BLUE_HEART + "Welcome to College Pet Life! I will guide you on your pet owner journey!")

    global player
    
    player =  input("What is your name?")
    print(f"Hello, {player}!")
    print("U+1F603" + " We are so happy that you have decided to adopt today!\n")
    print("----------------------------")
    print(HUNDRED_EMOJI + "As a pet owner, your goal is to ensure that your pet stays happy and healthy.")
    print(EXCLAIMATION + "Don't forget that as a first-time pet owner you only have 7 days with your pet until their first vet visit. \n Unfortunately, you cannot continue to have your pet if it reaches 0 health points.")


# pet directory
pet = {"name": "", "type":, "age": 0, "hunger": 0, "toys": []}
# pet Toys to play with 
petToys = {"dog": ["frisbee", "tennis ball", "tug rope"], "cat": ["ball of yarn", "scratching post", "feather pole"]}, "bunny": ["key rings", "rattle", "straw ball"] 


def choosePet(): -> None 
    """Choosing your own pet."""
    petType: str = ""
    
    petOptions = list(pet.keys())
    while petType not in petOptions:
        print("Please input a type of pet you would like to adopt from the following options:")
        for option in petOptions:
            print(option)
        petType = input("Please input one of the pets: ")
    print(petType)
    # add pet type into memory
    pet["type"] = petType
    # name your pet
    input(f"What would you like to name your {pet["type"]} ?")

def printMenu_Pet(menuOptions):
    optionKeys = list(menuOptions.keys())

    print("Here are the pets avaliable: ")
    print("----------------------------")
    for key in optionKeys: 
        print(key + "":\t" + menu.Options[key]["text"])


def feedPet():
    """Feed your pet to increase their health."""
    print("---------------Time to Eat---------------")
    global health
    global points

    if health <= 100: 
        health += 30
        print(PARTY_POP + "Wow someone's hungry! Your pet ate all their food and earned 30 health points.")
    
    if health >= 100:
        health = 100
        print("Your pet has over 100 health points. Feeding your pet wasn't necessary, but they still ate I guess. Anyways, your pet's health is now at 100 points!")
    points -= 5
    print("Eating too much was a little uncomfortable. Therefore, your pet's happyiness points decreased by 5.")
    print("-----------------------------------------")


def bond():
    """Choose to play and bond with your pet to increase happiness points."""
    outcome: int = random.randrange(0,8)
    point_count: int = random.randrange(10, 45)
    health_count: int = random.randrange(0, 25)
    choice: str = ""

    print("-----------------------------------------")

    global health
    global points

    if outcome == 0: 
        print("You want to teach your" {pet["type"]} "some tricks. \n You want your" {pet["type"]} "to be super smart.")
        print(BLUE_HEART+ "Do you choose to a) teach them how to shake hands or b) roll around?\n")
        if response == "a": 
            print("You taught your" {pet["type"]} "how to shake hands. It seems they were able to pick it up easily.")
            print(f"Teaching them how to shake hands made your {pet["type"]} so happy. You earned {point_count} points and they lost {health_point} health points.")
            points += point_count
            health -= health_count
        if response == "b":
            print(f"You taught your {pet["type"]} how to roll around. It seems that they were able to pick it up easily, a little too easily. \n They rolled around too much and got dizzy.)
            print(f"Your pet earn {point_count} points but all that rolling made them dizzy really easily, loosing 10 points.)
            points += point_count
            health -= health_count - 10

    # made an accident scold or praise
    if outcome == 1: 
        print("Oh no! Your" {pet["type"]} "made a small accident in your room! Not on the rug!.")
        print(BLUE_HEART + "Do you choose to a) scold them or b) shake it off? \n You'll still have to clean it either way. Gross!"
        if response == "a":
            print("You scolded them, clearly showing how annoyed you are with having to clean up the mess.")
            print(f"However, your {pet["type"]} got really sad and stayed away from you for the rest of the day.")
            print(f"Your pet lost happiness {point_count} points.") 
            points -= point_count
        if response == "b":
            print("It really wasn't a big deal so you shook it off. Wow such patience!")
            print(f"You try reasoning with your pet gently about what to do next time. Your pet earned happiness {point_count} point and gained {health_count} points.")
            points += point_count
            health += health_count

    # go take a walk around campus or nap together 
    if outcome == 2: 
        print("It's finally FALL! The weather is so nice today!")
        print(BLUE_HEART + "Do you choose to a) go for a walk with your pet around campus or b) stay in and take a nap together?")
        if response == "a":
            print("Oh that's so unfortunate! You went to go outside to talk around campus, but it starts pour really hard. \n Apparently, you forgot there was a hurricane coming.")
            print(f"Your pet get terrified of the gusty wind losing {point_count} points. Since you had to run back to your room, they lost {health_count} points.")
            points -= point_count
            health -= health_count
        if response == "b":
            print("You decide to take a nap together instead because both of you are tired from the long week. \n Luckly, you slept throught the aweful hurricane.")
            print(f"Your pet feels so energized right now that they earned {point_count} happiness points and {health_count} points.")

    #  stock up on toy items at the toy store or create an instagram for your pet
    if outcome == 3: 
        print("Your pet is feeling bored and want to do something exciting to do.")
        print(BLUE_HEART + "Do you choose to a) go stock up on toys at the pet store or b) create an instagram for your pet?")

        if response == "a":
            print("You decide to walk to the nearest pet store to pick up from the pet store.")
            print(f"Your pet enjoyed picking all their favorite toys and seeing other pets, earning {point_count} happiness points. \n But they got tired with all the walking from your room to the petstore, losing {health_count} points.")
            points += point_count
            health -= health_count
        if response == "b":
            print("You decide to create an instagram account for your pet.")
            print(f"Your pet certaintly does all love all the attention, increasing their happiness to {point_count} points. \n But they got tired with all the pictures you had to take, decreasing their health energy {health_count} points.")
            points += point_count
            health -= health_count

    # picking what toys to play with 
    if outcome == 4: 
        print("Now that you bought so much toys for your pet, it's time to finally play with them!")
        toyChoices = petToys[pet["type"]]
        toyNum = - 1 
        while toyNum < 0 or toyNum > len(petToys):
            print("Here are your choices:")
            for i in range(len(toyChoices)):
                print(str(i) + ":" + toyChoices[i])
            toyNum = int(input("Please input what toy to play with: "))  

        chosen_Toy = toyOptions[toyNum]
        pet["toys"].append(chosenToy)
        print("Great! You selected the" + chosen_Toy + !")
        print(BLUE_HEART + "Do you want to play a) inside or b) outside?")
        if response == "a":
            print("You decide to play inside in your room with the" + chosen_Toy + " with your pet.")
            print(f"Your pet enjoyed playing inside with you and earned {point_count} happiness points, but depleted their energery {health_count} points.")
            points += point_count
            health -= health_count
        if response == "b":
            print("You decide to play inside in your room with the" + chosen_Toy + " with your pet.")
            print(f"Your pet enjoyed playing outside with you and earned {point_count} happiness points, but all that running made them super dirty, leaving mud all around your room, loosing {health_point} points.")
            points += point_count
            health -= health_count

    # give them a bath or make them treats
    if outcome == 5: 
        print("It a day to stay inside your room and just chill with your pet.")
        print(BLUE_HEART + "Do you decide to a) give them a bath or b) make them some homemade treats?")

        if response == "a":
            print("You realize that your pet has gotten really dirty and needs a bath.")
            print(f"While your pet was scared of the water first, they realize that it was so refreshing and earned {point_count} happiness points, adding {health_count} health points.")
            points += point_count
            health += health_count
        if response == "b":
            print("You decide to make some homemade pet treats based on a recipe you found on a blog.")
            print(f"While your pet enjoyed eating those yummy treats, the secret ingredient you added caused them to throw up. They lost {point_count} happines points and {healht_count} points. Disgusting!")
            points -= point_count
            health -= health_count

    # meeting new pets
    if outcome == 6: 
        print("Looks like other students are bringing their pets to a picnic at the Quad.")
        print(BLUE_HEART + "Do you allow a) your pet to meet other pets or b) stay by your side at all times?"
            
        if response == "a":
            print("You decide to let your pet meet the other pets while you catch up with your friends.")
            print(f"")
            points += point_count
            health -= health_count
        if response == "b":
            print("You were afraid that you might loose sight of your pet and decide to keep them at your side at all times.")
            print(f"")
            points += point_count
            health += health_count

    # dressing up your pet or brining your friends over
     if outcome == 7: 
        print("You finishied your homework early and have a lot of free time later tonight. Halloween season is coming soon.")
        print(BLUE_HEART + "Do you decide a) to play dress up with your pet or b) bring your friends over to hang out with your pet?")
            
        if response == "a":
            print("You decide that your can hang out with your friends sometime else and instead play dress up with your pet to finalize Halloween costumes.")
            print(f"Wow! So so many options this year. Despite that your room is a total mess, your pet loved all of your ideas, earning them {point_count} happiness points and {health_point} points.")
            points += point_count
            health += health_count

        if response == "b":
            print("You decide to invite your friends over to fianlly meet your pet! \n Looks like they absolutley adore them!")
            print(f"Your pet enjoyed all the attention and extra treats, increasing {point_count} happiness points, but realized that they got super tired, decreasing their {health_count} points.")
            points += point_count
            health -= health_count

    print("-----------------------------------------")


def menu() -> None:
    """Ask player their actions for the game."""
    continue_playing: bool = True
    day: int = 0

    while continue_playing is True:
        #print() style design 
        choice: int: int(input(BLUE_HEART + "Enter 0 to check on your pet's health, 1 to feed, 2 to play, or 3 to exit the game: "))
        if choice == 0:
            #status(day)
        elif choice == 1:
            feedPet()
            day += 1 
        elif choice == 2:
            bond()
            day += 1
        elif choice == 3: 
            print("Oh leaving already? We are so exited to see you soon! Game exited.")
            continue_playing = False
        
        if health < 0:
            print(PLEAD_FACE + "Oh noooo! You neglected your pet. It got too sick and depressed. Game over.")
        if day > 7:
            print("It's time for your pet's first vet visit! Come back later! Game over.")
        if points < 100:
            print (EXCLAIMATION + "---------------LOSER-------------- " + EXCLAIMATION)
            print(f"Unfortunately, your pet did not reach 100 health point. You ended up with {point} pet owner points. Your pet needs more attention and care.")
        if points > 100:
            print (PARTY_POP + "---------------WINNER--------------" + PARTY_POP)
            print(f"Great job! Your pet is happy and healthy! Your total pet owner points were: {points}")
        print("----------------------------")


if __name__ == "__main__":
    main()