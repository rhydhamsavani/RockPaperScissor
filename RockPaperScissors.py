import random 

f = "1"
while f == "1":
    
        print ("Welcome to Rock, Paper, and Scissors")
        game = ["rock", "paper", "scissors"]

        while True:
            random_index = random.randint(0,2)
            cpu_choice = game[random_index]

            userchoice = input("choose rock, paper or scissors: ").lower()
            while userchoice not in game:
                userchoice = input("This is not an invalid input, please try again: ").lower()

            print("your choice: ", userchoice)
            print("computer choice: ", cpu_choice)

            if userchoice == 'rock':
                if cpu_choice == 'rock':
                    print ("it is a tie")
                elif cpu_choice == 'paper':
                    print ("You lost!")
                elif cpu_choice == 'scissors':
                    print ("You win!")

            elif userchoice == 'paper':
                if cpu_choice == 'paper':
                    print ("It is a tie!")
                elif cpu_choice == 'scissors':
                    print ("You lost!")
                elif cpu_choice == 'rock':
                    print ("You win!")

            elif userchoice == 'scissors':
                if cpu_choice == 'scissors':
                    print ("It is a tie!")
                elif cpu_choice == 'rock':
                    print ("You lost!")
                elif cpu_choice == 'paper':
                    print ("You win!")

            f = input("""Would you like to play again?
                            1. for yes
                            2. for no.\n """)

                    



    




