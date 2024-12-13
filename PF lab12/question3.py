import random
dice1 = [1, 2, 3, 4, 5, 6]
dice2 = [1, 2, 3, 4, 5, 6]

def roll_dice(dice):
    return random.choice(dice)
def play_game():
    # Player 1 rolls the dice
    player1_roll = roll_dice(dice1)
    print(f"Player 1 rolled: {player1_roll}")
    # Player 2 rolls the dice
    player2_roll = roll_dice(dice2)
    print(f"Player 2 rolled: {player2_roll}")
    if player1_roll > player2_roll:
        print("Player 1 wins!")
    elif player2_roll > player1_roll:
        print("Player 2 wins!")
    else:
        print("It's a tie!")
play_game()
