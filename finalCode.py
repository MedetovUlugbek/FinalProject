import gameProfile
import quests

# This code creates a loop where, after setting up the character, player can go and complete different chapters in form of quests.
# There is no specific order for quest completion. When Player completes the quest of his/her choice, he won't be able to do it again.
def main():
    gameProfile.playerInfo()
    gameProfile.playerNameAssignment()
    gameProfile.playerClassSelection()
    gameProfile.playerPowerIncreaseItems()
    gameProfile.playerProfile()
    
    while True:
        print("\nWhat would you like to do next?")
        print("1. Fight the goblin")
        print("2. Search for the lost horses")
        print("3. Exit game")
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == "1":
            quests.goblinFight()
        elif choice == "2":
            quests.horseSearching()
        elif choice == "3":
            print("Thank you for playing! Goodbye.")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()
