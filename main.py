### Create a rpg game that takes user input and uses it to create a story
### You are Hercules, the greatest of the Greek Heroes! You have been tasked by King Eurysthesus to slay the vicious Nemean Lion, defeat the impossible nine-headed Lernaean Hydra, and capture the guard dog of the underworld -- Cerberus!
### as a user, I want an engaging story to be told using print statements
### as a user, I want Hercules (and each enemy), to have health, attack power, a list of attacks names saved in a dictionary.
### as a user, I want the ability to select Hercules' attack using a menu prompt
### as a user, I want the foe's attack to be chosen randomly
### as a user, I want the results of each attack to be printed to the screen
### as a devloper, I want to use an Attack() function that will terminate when Hercules or the enemy's health reaches 0
### as a devloper, I want my RunGame() function to call my other functions in a logical order that will determine game flow

import random

## create a dictionary of the characters
## each character will have a name, health, attack power, and a list of attacks

Hercules = {
    "name": "Hercules",
    "health": 100,
    "attack power": 30,
    "attacks": ["Punch", "Kick", "Headbutt"]
}

Nemean_Lion = {
    "name": "Nemean Lion",
    "health": 100,
    "attack power": 10,
    "attacks": ["Bite", "Claw", "Roar"]
}

Lernaean_Hydra = {
    "name": "Lernaean Hydra",
    "health": 200,
    "attack power": 20,
    "attacks": ["Bite", "Claw", "Roar"]
}

Cerberus = {
    "name": "Cerberus",
    "health": 300,
    "attack power": 30,
    "attacks": ["Bite", "Claw", "Roar"]
}
## creates a function that will print the story menu
def Menu():
    print("1. Fight the Nemean Lion")
    print("2. Fight the Lernaean Hydra")
    if Nemean_Lion_Hide == True and Lernaean_Hydra_Blood == True:
        print("3. Fight Cerberus")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        Nemean_Lion_Fight()
    elif choice == 2:
        Lernaean_Hydra_Fight()
    elif choice == 3:
        Cerberus_Fight()
    else:
        print("Invalid choice. Try again.")
        Menu()
## create a function that prints the attack menu
def Attack_Menu():
    print("1. Punch")
    print("2. Kick")
    print("3. Headbutt")
    choice = int(input("Enter your choice: "))
    return choice

## create a function that will run the attack
def Attack(attacker, defender):
    choice = Attack_Menu()
    if choice == 1:
        print(attacker["name"] + " used Punch!")
        defender["health"] -= attacker["attack power"]
        print(defender["name"] + " has " + str(defender["health"]) + " health left!")
    elif choice == 2:
        print(attacker["name"] + " used Kick!")
        defender["health"] -= attacker["attack power"]
        print(defender["name"] + " has " + str(defender["health"]) + " health left!")
    elif choice == 3:
        print(attacker["name"] + " used Headbutt!")
        defender["health"] -= attacker["attack power"]
        print(defender["name"] + " has " + str(defender["health"]) + " health left!")
    else:
        print("Invalid choice. Try again.")
    if defender["health"] > 0:
        defender_choice = random.randint(1,3)
        if defender_choice == 1:
            print(defender["name"] + " used Bite!")
            attacker["health"] -= defender["attack power"]
            print(attacker["name"] + " has " + str(attacker["health"]) + " health left!")
        elif defender_choice == 2:
            print(defender["name"] + " used Claw!")
            attacker["health"] -= defender["attack power"]
            print(attacker["name"] + " has " + str(attacker["health"]) + " health left!")
        elif defender_choice == 3:
            print(defender["name"] + " used Roar!")
            attacker["health"] -= defender["attack power"]
            print(attacker["name"] + " has " + str(attacker["health"]) + " health left!")
    if attacker["health"] <= 0:
        print("You have died!")
        print("Game Over!")
        exit()
    elif defender["health"] <= 0:
        print(defender["name"] + " has died!")
        print("You win!")
        exit()

## print the beginning first part of the story
## here Hercules fights the Nemean Lion
## run a function that will have Hercules fight the Nemean Lion
def Nemean_Lion_Fight():
    print("The Nemean Lion is a ferocious beast with a hide so tough that no weapon can pierce it. You must defeat it with your bare hands!")
    while Hercules["health"] > 0 and Nemean_Lion["health"] > 0:
        Attack(Hercules, Nemean_Lion)
    if Nemean_Lion["health"] <= 0:
        Nemean_Lion_Hide()

## print the end of the first part of the story
## run a function that increse Hercules' health by 20 and completes the Nemean Lion fight
def Nemean_Lion_Hide():
    print("You have defeated the Nemean Lion!")
    print("You have obtained the Nemean Lion's hide!")
    print("You have increased your health by 20!")
    Hercules["health"] += 20
    print("You now have " + str(Hercules["health"]) + " health!")
    print("You have completed the first task of King Eurysthesus!")
    print("You have been given a new task!")
    print("You must now defeat the Lernaean Hydra!")
    Menu()
## print the second part of the story
## here Hercules fights the Lernaean Hydra
## run a function that have Hercules fight the Lernaean Hydra
def Lernaean_Hydra_Fight():
    print("The Lernaean Hydra is a monster with nine heads. You must defeat it with your bare hands!")
    while Hercules["health"] > 0 and Lernaean_Hydra["health"] > 0:
        Attack(Hercules, Lernaean_Hydra)
    else:
        Lernaean_Hydra_Blood()

## print the end of the second part of the story
## run a function that increse Hercules' health by 20 and completes the Lernaean Hydra fight
def Lernaean_Hydra_Blood():
    print("You have defeated the Lernaean Hydra!")
    print("You have obtained the Lernaean Hydra's blood!")
    print("You have increased your health by 20!")
    Hercules["health"] += 20
    print("You now have " + str(Hercules["health"]) + " health!")
    print("You have completed the second task of King Eurysthesus!")
    print("You have been given a new task!")
    print("You must now defeat Cerberus!")
    Menu()

## print the beginning of the third part of the story
## here Hercules fights Cerberus
## run a function that have Hercules fight Cerberus
def Cerberus_Fight():
        print("Cerberus is the three-headed guard dog of the Underworld. You must defeat it with your bare hands!")
        while Hercules["health"] > 0 and Cerberus["health"] > 0:
            Attack(Hercules, Cerberus)
        else:
            Cerberus_Tail()

## print the end of the third part of the story
## run a function that completes the Cerberus fight and brings the story to an end
def Cerberus_Tail():
    print("You have defeated Cerberus!")
    print("You have obtained Cerberus' tail!")
    print("You have completed the third task of King Eurysthesus!")
    print("You have completed all of King Eurysthesus' tasks!")
    print("You have completed the story!")
    print("You have won the game!")
    exit()
## print the end of the story
print("King Eurysthesus stands in shock as you bring back Cerberus and the other trophies!\n\nYou have earned the hand of Princess Megara!\n\nYou have reached the end of the game!\nThanks for playing!")
## create a function that will run the game
def RunGame():
    Menu()