"""EX06 Choose Your Own Adventure: College Dog Life."""

__author__ = "730569341"

import random

"""Assigning global variables."""

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
    print(BLUE_HEART + "Welcome to College dog Life! I will guide you on your dog owner journey!")

    global player
    
    player = input("What is your name?")
    print(f"Hello, {player}!")
    print("U+1F603" + " We are so happy that you have decided to adopt today!\n")
    print("----------------------------")
    print(HUNDRED_EMOJI + "As a dog owner, your goal is to ensure that your dog stays happy and healthy.")
    print(EXCLAIMATION + "Don't forget that as a first-time dog owner you only have 7 days with your dog until their first vet visit. \n Unfortunately, you cannot continue to have your dog if it reaches 0 health points.")


def feed():
    """Feed your dog to increase their health."""
    print("---------------Time to Eat---------------")
    global health
    global points

    if health <= 100: 
        health += 30
        print(PARTY_POP + "Wow someone's hungry! Your dog ate all their food and earned 30 health points.")
    
    if health >= 100:
        health = 100
        print("Your dog has over 100 health points. Feeding your dog wasn't necessary, but they still ate I guess. Anyways, your dog's health is now at 100 points!")
    points -= 5
    print("Eating too much was a little uncomfortable. Therefore, your dog's happyiness points decreased by 5.")
    print("-----------------------------------------")


def bond():
    """Choose to play and bond with your dog to increase happiness points."""
    outcome: int = random.randrange(0, 8)
    point_count: int = random.randrange(10, 45)
    health_count: int = random.randrange(0, 25)
    choice: str = ""

    print("-----------------------------------------")

    global health
    global points

    if outcome == 0: 
        print("You want to teach your dog some tricks. \n You want your dog to be super smart.")
        print(BLUE_HEART + "Do you choose to a) teach them how to shake hands or b) roll around?")
        if choice == "a": 
            print("You taught your dog how to shake hands. It seems they were able to pick it up easily.")
            print(f"Teaching them how to shake hands made your dog so happy. You earned {point_count} points and they lost {health_count} health points.")
            points += point_count
            health -= health_count
        if choice == "b":
            print("You taught your dog how to roll around. It seems that they were able to pick it up easily, a little too easily. \n They rolled around too much and got dizzy.")
            print(f"Your dog earn {point_count} points but all that rolling made them dizzy really easily, loosing 10 points.")
            points += point_count
            health -= health_count - 10

    # made an accident scold or praise
    if outcome == 1: 
        print("Oh no! Your dog made a small accident in your room! Not on the rug!.")
        print(BLUE_HEART + "Do you choose to a) scold them or b) shake it off? \n You'll still have to clean it either way. Gross!")
        if choice == "a":
            print("You scolded them, clearly showing how annoyed you are with having to clean up the mess.")
            print("However, your dog got really sad and stayed away from you for the rest of the day.")
            print(f"Your dog lost happiness {point_count} points.") 
            points -= point_count
        if choice == "b":
            print("It really wasn't a big deal so you shook it off. Wow such patience!")
            print(f"You try reasoning with your dog gently about what to do next time. Your dog earned happiness {point_count} point and gained {health_count} points.")
            points += point_count
            health += health_count

    # go take a walk around campus or nap together 
    if outcome == 2: 
        print("It's finally FALL! The weather is so nice today!")
        print(BLUE_HEART + "Do you choose to a) go for a walk with your dog around campus or b) stay in and take a nap together?")
        if choice == "a":
            print("Oh that's so unfortunate! You went to go outside to talk around campus, but it starts pour really hard. \n Apparently, you forgot there was a hurricane coming.")
            print(f"Your dog get terrified of the gusty wind losing {point_count} points. Since you had to run back to your room, they lost {health_count} points.")
            points -= point_count
            health -= health_count
        if choice == "b":
            print("You decide to take a nap together instead because both of you are tired from the long week. \n Luckly, you slept throught the aweful hurricane.")
            print(f"Your dog feels so energized right now that they earned {point_count} happiness points and {health_count} points.")

    #  stock up on toy items at the toy store or create an instagram for your dog
    if outcome == 3: 
        print("Your dog is feeling bored and want to do something exciting to do.")
        print(BLUE_HEART + "Do you choose to a) go stock up on toys at the dog store or b) create an instagram for your dog?")

        if choice == "a":
            print("You decide to walk to the nearest dog store to pick up from the dog store.")
            print(f"Your dog enjoyed picking all their favorite toys and seeing other dogs, earning {point_count} happiness points. \n But they got tired with all the walking from your room to the dogstore, losing {health_count} points.")
            points += point_count
            health -= health_count
        if choice == "b":
            print("You decide to create an instagram account for your dog.")
            print(f"Your dog certaintly does all love all the attention, increasing their happiness to {point_count} points. \n But they got tired with all the pictures you had to take, decreasing their health energy {health_count} points.")
            points += point_count
            health -= health_count

    # picking what toys to play with 
    if outcome == 4: 
        print("Now that you bought so much toys for your dog, it's time to finally play with them!")
       
        print(BLUE_HEART + "Do you want to play a) inside or b) outside?")
        if choice == "a":
            print("You decide to play inside in your room with your dog.")
            print(f"Your dog enjoyed playing inside with you and earned {point_count} happiness points, but depleted their energery {health_count} points.")
            points += point_count
            health -= health_count
        if choice == "b":
            print("You decide to play inside in your room with your dog.")
            print(f"Your dog enjoyed playing outside with you and earned {point_count} happiness points, but all that running made them super dirty, leaving mud all around your room, loosing {health_count} points.")
            points += point_count
            health -= health_count

    # give them a bath or make them treats
    if outcome == 5: 
        print("It a day to stay inside your room and just chill with your dog.")
        print(BLUE_HEART + "Do you decide to a) give them a bath or b) make them some homemade treats?")

        if choice == "a":
            print("You realize that your dog has gotten really dirty and needs a bath.")
            print(f"While your dog was scared of the water first, they realize that it was so refreshing and earned {point_count} happiness points, adding {health_count} health points.")
            points += point_count
            health += health_count
        if choice == "b":
            print("You decide to make some homemade dog treats based on a recipe you found on a blog.")
            print(f"While your dog enjoyed eating those yummy treats, the secret ingredient you added caused them to throw up. They lost {point_count} happines points and {health_count} points. Disgusting!")
            points -= point_count
            health -= health_count

    # meeting new dogs
    if outcome == 6: 
        print("Looks like other students are bringing their dogs to a picnic at the Quad.")
        print(BLUE_HEART + "Do you allow a) your dog to meet other dogs or b) stay by your side at all times?")
            
        if choice == "a":
            print("You decide to let your dog meet the other dogs while you catch up with your friends.")
            print(f"Your dog met some new friends and earned {point_count} happiness points, but got tired running around the Quad, decreasing their health points by {health_count}.")
            points += point_count
            health -= health_count
        if choice == "b":
            print("You were afraid that you might loose sight of your dog and decide to keep them at your side at all times.")
            print(f"Your dog just stayed on their leash beside your the whole time while you talked to your friends which wasn't that great. \n This decreased their happiness by {point_count} points, but at leas they got to nap, increasing their health by {health_count} points.")
            points -= point_count
            health += health_count

    # dressing up your dog or brining your friends over
    if outcome == 7: 
        print("You finishied your homework early and have a lot of free time later tonight. Halloween season is coming soon.")
        print(BLUE_HEART + "Do you decide a) to play dress up with your dog or b) bring your friends over to hang out with your dog?")
            
        if choice == "a":
            print("You decide that your can hang out with your friends sometime else and instead play dress up with your dog to finalize Halloween costumes.")
            print(f"Wow! So so many options this year. Despite that your room is a total mess, your dog loved all of your ideas, earning them {point_count} happiness points and {health_count} points.")
            points += point_count
            health += health_count

        if choice == "b":
            print("You decide to invite your friends over to fianlly meet your dog! \n Looks like they absolutley adore them!")
            print(f"Your dog enjoyed all the attention and extra treats, increasing {point_count} happiness points, but realized that they got super tired, decreasing their {health_count} points.")
            points += point_count
            health -= health_count

    print("-----------------------------------------")


def menu() -> None:
    """Ask player their actions for the game."""
    continue_playing: bool = True
    day: int = 0

    while continue_playing is True:
        choice = int(input(BLUE_HEART + "Enter 0 to check on your dog's health, 1 to feed, 2 to play, or 3 to exit the game: "))
        if choice == 0:
            print(day)
        elif choice == 1: 
            feed()
            day += 1 
        elif choice == 2:
            bond()
            day += 1
        elif choice == 3: 
            print("Oh leaving already? We are so exited to see you soon! Game exited.")
            continue_playing = False
        
        if health < 0:
            print(PLEAD_FACE + "Oh noooo! You neglected your dog. It got too sick and depressed. Game over.")
        if day > 7:
            print("It's time for your dog's first vet visit! Come back later! Game over.")
        if points < 100:
            print(EXCLAIMATION + "---------------LOSER-------------- " + EXCLAIMATION)
            print(f"Unfortunately, your dog did not reach 100 health point. You ended up with {points} dog owner points. Your dog needs more attention and care.")
        if points > 100:
            print(PARTY_POP + "---------------WINNER--------------" + PARTY_POP)
            print(f"Great job! Your dog is happy and healthy! Your total dog owner points were: {points}")
        print("----------------------------")


if __name__ == "__main__":
    main()