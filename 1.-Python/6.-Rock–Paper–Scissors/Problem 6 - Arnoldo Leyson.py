Python 3.6.8 (v3.6.8:3c6b436a57, Dec 24 2018, 02:04:31) 
[GCC 4.2.1 Compatible Apple LLVM 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> ##1. Import the choice function of the random module.
>>> import random
>>> 
>>> ##2. Create a list that includes the 3 possible gesture options of the game: 'rock', 'paper' or 'scissors'. Store the list in a variable called gestures.
>>> gestures = ['rock', 'paper', 'scissors']
>>> 
>>> ##3. Create a variable called n_rounds to store the maximum number of rounds to play in a game.
>>> n_rounds = 5
>>> 
>>> ##4. Create a variable called rounds_to_win to store the number of rounds that a player must win to win the game.
>>> rounds_to_win = round((n_rounds+0.5)/2)
>>> print("Rounds to win:", rounds_to_win)
Rounds to win: 3
>>> ##5. Create two variables to store the number of rounds that the computer and the player have won. Call these variables cpu_score and player_score.
>>> cpu_score = 0
>>> player_score = 0
>>> tie_score = 0
>>> 
>>> ##6. Define a function that randomly returns one of the 3 gesture options.
>>> random.choice(gestures)
'paper'
>>> 
>>> ##7. Define a function that asks the player which is the gesture he or she wants to show: 'rock', 'paper' or 'scissors'.
>>> player_choice = input ('Choose: rock, paper or scissors (write in lowercase):')
Choose: rock, paper or scissors (write in lowercase):rock
>>> while (player_choice != "rock") & (player_choice != "paper") & (player_choice != "scissors"):
	player_choice = input ('Choose: rock, paper or scissors:')

	
>>> ##8. Define a function that checks who won a round.
>>> ##9. Define a function that prints the choice of the computer, the choice of the player and a message that announces who won the current round.
>>> ##10. Now it's time to code the execution of the game using the functions and variables you defined above.
>>> ##11. Print the winner of the game based on who won more rounds.
>>> 
>>> round_number = 0
>>> 
>>> while True:
    print ("Round:", round_number+1)
    player_choice = input ("What is your choice: rock, paper or scissors?")
    cpu_choice = random.choice(gestures)
    print ("Player choice:", player_choice)
    print ("CPU choice:", cpu_choice)
    if player_choice == cpu_choice:
        print ("Result: Draw, Let's repeat this round:")
        tie_score = tie_score + 1
        round_number = round_number
    elif (player_choice == "rock") and (cpu_choice == "paper"):
        print ("Result: CPU wins")
        cpu_score = cpu_score + 1
        round_number = round_number + 1
        if cpu_score >= rounds_to_win:
            print("CPU won the game")
            break
    elif (player_choice == "rock") and (cpu_choice == "scissors"):
        print ("Result: You win")
        player_score = player_score + 1
        round_number = round_number + 1
        if player_score >= rounds_to_win:
            print("You won the game")
            break
    elif (player_choice == "paper") and (cpu_choice == "scissors"):
        print ("Result: CPU wins")
        cpu_score = cpu_score + 1
        round_number = round_number + 1
        if cpu_score >= rounds_to_win:
            print("CPU won the game")
            break
    elif (player_choice == "paper") and (cpu_choice == "rock"):
        print ("Result: You win")
        player_score = player_score + 1
        round_number = round_number + 1
        if player_score >= rounds_to_win:
            print("You won the game")
            break
    elif (player_choice == "scissors") and (cpu_choice == "rock"):
        print ("Result: CPU wins")
        cpu_score = cpu_score + 1
        round_number = round_number + 1
        if cpu_score >= rounds_to_win:
            print("CPU won the game")
            break
    elif (player_choice == "scissors") and (cpu_choice == "paper"):
        print ("Result: You win")
        player_score = player_score + 1
        round_number = round_number + 1
        if player_score >= rounds_to_win:
            print("You won the game")
            break
    else:
        print ("Invalid choice, Let's try again!")
    round_number = round_number
    if round_number >= n_rounds:
        break

Round: 1
What is your choice: rock, paper or scissors?rock
Player choice: rock
CPU choice: scissors
Result: You win
Round: 2
What is your choice: rock, paper or scissors?rock
Player choice: rock
CPU choice: paper
Result: CPU wins
Round: 3
What is your choice: rock, paper or scissors?rock
Player choice: rock
CPU choice: rock
Result: Draw, Let's repeat this round:
Round: 3
What is your choice: rock, paper or scissors?rock
Player choice: rock
CPU choice: scissors
Result: You win
Round: 4
What is your choice: rock, paper or scissors?rock
Player choice: rock
CPU choice: scissors
Result: You win
You won the game
>>> 
