import random
import time
global counter
counter=0

def increment_counter():
    global counter
    counter+=1

def game():
    choices = ["rock","paper","scissors"]
    while True:
        print("What will you choose?\n[Rock|Paper|Scissors]\n")
        user_choice=input("Choice: ").lower().strip()
        computer_choice= random.choice(choices)
        time.sleep(2)
        print("Computer chooses",computer_choice)
        if user_choice==computer_choice:
            print("It's a draw!")
        elif user_choice == choices[0] and computer_choice == choices[2]:
            print("You win!")
            increment_counter()
        elif user_choice == choices[1] and computer_choice == choices[0]:
            print("You win!")
            increment_counter()
        elif user_choice == choices[2] and computer_choice == choices[1]:
            print("You win!")
            increment_counter()
        else:
            print("You lose!")
        print("\n")
        user_choice=input("Do you want to play again? [Yes/No]: ").lower().strip()
        if user_choice!='yes' and user_choice!='y':
            print("\n")
            menu()
            break
def stats():
    while True:
        print(f"You currently have {counter} wins against the computer!")
        user_choice=input("\n Go back? [Yes/No]:")
        print("\n")
        if user_choice!= 'yes' and user_choice!='y':
            print("\n")
            exit()
        else:
            menu()

def menu():
    while True:
        try:
            print("===Main Menu===")
            print("[1]Play Game\n[2]Show stats\n[3]Exit")
            print("===============")
            user_choice=int(input("Choice: "))
            print("\n")
            match user_choice:
                case 1:
                    game()
                case 2:
                    stats()
                case 3:
                    exit()
        except ValueError:
            print("Invalid Input. Please enter the valid choices.\n")



print("Welcome to Rock Paper Scissors!\nPress enter to start!")
user_choice= input("")
menu()