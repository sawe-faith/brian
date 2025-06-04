import random
def main():
    get_number(3)

def get_number(n):
    rolls = n
    counter = 0  
    while rolls > 0:
        choice = input(f"Roll the dice? You have {rolls} rolls remaining. (y/n): ").lower()
        if choice == 'y':
            die1 = random.randint(1, 6)
            die2 = random.randint(1, 6)
            print(f"{die1}, {die2}")
            rolls -= 1
            counter += 1
            print("Counter: ", counter)
        elif choice == 'n':
            print("Thanks for playing!")
            break
        else:
            print("Invalid Choice!!")
            continue 
    if rolls == 0:
        print("You have rolled to the maximum. Thanks for Playiing!")       
if __name__ == "__main__":
    main()