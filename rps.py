import random

def game():
    computer_move = random.randrange(3)
    player_move = input("Rock,Paper,Scissors? ")

    if player_move == "rock":
        player_move = 0
    elif player_move == "paper":
        player_move = 1
    elif player_move == "scissors":
        player_move = 2
    else:
        print("Unrecognized move restarting game. If you think this is not correct please contact Rudyon.")
        game()

    if computer_move == 0:
        print("Computer played rock!")
    elif computer_move == 1:
        print("Computer played paper!")
    elif computer_move == 2:
        print("Computer played scissors!")

    if player_move == computer_move:
        print("It's a Draw!")
    elif player_move == 0 and computer_move == 2 or player_move == 1 and computer_move == 0 or player_move == 2 and computer_move == 1:
        print("You win!")
    elif player_move == 0 and computer_move == 1 or player_move == 1 and computer_move == 2 or player_move == 2 and computer_move == 0:
        print("You lose. :(")

    play_again = input("Play again?[y|n] ")

    if play_again == "y":
        game()
    elif play_again == "n":
        print("Thank you for playing!")
    else:
        print("Unrecognized move restarting game. If you think this is not correct please contact Rudyon.")
        game()

game()