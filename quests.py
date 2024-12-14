# This is a second part of the game, after players passes the first chapter of the game.
# This file contains 2 chapters in forms of quests. Player can choose any of two quests that are available as of right now.
import gameProfile

def goblinFight():
    questNPC = "Lily"
    print(f"{questNPC}: Hello. Would you like to go on a goblin fighting quest? (Y/N)")
    answer = input()
    if answer.upper() == "Y":
        print("There are several goblins seen nearby a village. Kill the goblins to keep the villagers safe.")
        numberOfGoblins = 5
        goblinsKilled = 0

        while numberOfGoblins > goblinsKilled:
            print("Fighting the Goblins...")
            print("Type 'KILL' to kill a goblin or 'exit' to quit the quest.")
            action = input()
            if action.upper() == "KILL":
                goblinsKilled += 1
                print(f"Great. You have defeated a goblin. Goblins killed: {goblinsKilled}/{numberOfGoblins}")
            elif action.upper() == "EXIT":
                print(f"You couldn't defeat all the goblins. Try again next time.")
                break
            else:
                print("Invalid input. Please type 'find' or 'exit'.")
        
        if goblinsKilled == numberOfGoblins:
            print("Amazing. Villagers are expressing their gratitude to you.")

    elif answer.upper() == "N":
        print("Enjoy the rest of the day!")

    else:
        print("Please choose either 'Y' or 'N'")

def horseSearching():
    questNPC = "Lily"
    print(f"{questNPC}: Hello. Would you like to go on a horse searching quest? (Y/N)")
    answer = input()
    if answer.upper() == "Y":
        print("There are a several horses lost in the forest. Find and return them to the farmer")
        numberOfHorses = 3
        horsesFound = 0

        while numberOfHorses > horsesFound:
            print("Searching the Forest...")
            print("Type 'find' to locate a lost horse or 'exit' to quit the quest.")
            action = input()
            if action.upper() == "FIND":
                horsesFound += 1
                print(f"Great. You have found a horse. Horses found: {horsesFound}/{numberOfHorses}")
            elif action.upper() == "EXIT":
                print(f"You couldn't find all the horses. Try again next time.")
                break
            else:
                print("Invalid input. Please type 'find' or 'exit'.")
        
        if horsesFound == numberOfHorses:
            print("Amazing. Farmer is grateful to you.")
        
    elif answer == "N":
        print("Enjoy the rest of the day!")
    
    else:
        print("Please choose either 'Y' or 'N'")
