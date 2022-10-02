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
## print the beginning first part of the story
## here Hercules fights the Nemean Lion
print("The Nemean Lion is a ferocious beast with a hide so tough that no weapon can pierce it. You must defeat it with your bare hands!")

## print the end of the first part of the story
print("You have defeated the Nemean Lion!")

## run a function that increse Hercules' health by 20
def Nemean_Lion_Hide():
    Hercules["health"] += 20
    print("Hercules' health is now " + str(Hercules["health"]))
    print("You have earned the Nemean Lion's hide as a trophy!")

## print the second part of the story
## here Hercules fights the Lernaean Hydra
print("The Lernaean Hydra is a nine-headed serpent with a poisonous bite. You must defeat it!")

## print the end of the second part of the story
print("You have defeated the Lernaean Hydra!")

## run a function that increse Hercules' health by 20
def Lernaean_Hydra_Blood():
    Hercules["health"] += 20
    print("Hercules' health is now " + str(Hercules["health"]))
    print("You have earned the Lernaean Hydra's blood as a trophy!")

## print the beginning of the third part of the story
## here Hercules fights Cerberus
print("Cerberus is the three-headed guard dog of the Underworld. You must capture it and bring it back to King Eurysthesus!")

## print the end of the third part of the story
print("You have captured Cerberus!")

## print the end of the story
print("You have brought Cerberus back to King Eurysthesus!\nYou have completed your tasks and are now the greatest of the Greek Heroes!\nYou have earned the hand of Princess Megara!")

## run a function that increse Hercules' health by 20
def Cerberus_Tongue():
    Hercules["health"] += 20
    print("Hercules' health is now " + str(Hercules["health"]))
    print("You have earned Cerberus' tongue as a trophy!")

## create a function that will run the game
def RunGame():
    Nemean_Lion_Hide()
    Lernaean_Hydra_Blood()
    Cerberus_Tongue()