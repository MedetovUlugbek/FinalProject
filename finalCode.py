import m1
import m2

def main():
    m1.playerInfo()
    m1.playerNameAssignment()
    m1.playerClassSelection()
    m1.playerPowerIncreaseItems()
    m1.playerProfile()
    
    while True:
        print("\nWhat would you like to do next?")
        print("1. Fight the goblin")
        print("2. Search for the lost horses")
        print("3. Exit game")
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == "1":
            m2.goblinFight()
        elif choice == "2":
            m2.horseSearching()
        elif choice == "3":
            print("Thank you for playing! Goodbye.")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()