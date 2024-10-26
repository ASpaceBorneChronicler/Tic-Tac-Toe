import prettytable as pt
import os

tic_table = pt.PrettyTable(header=False, hrules=1)

def check_win(plays):
    win_conditions = [
        [1,2,3],
        [4,5,6],
        [7,8,9],
        [1,4,7],
        [2,5,8],
        [3,6,9],
        [1,5,9],
        [3,5,7]
    ]
    return any([all([position in plays for position in condition]) for condition in win_conditions])

game_table = [
                [1,2,3],
                [4,5,6],
                [7,8,9]
            ]

tic_table.add_rows(game_table)

def tic_tac_toe():
    x_plays = []
    l_plays = []
    
    moves = {num: (i // 3, i % 3) for i, num in enumerate(range(1, 10))}

    player = "X"

    for _ in range(9):
        # Handle input
        while True:

            # Show table
            print(tic_table)
            
            try:
                player_input = int(input(f"Player {player} make your move:\n(Input the number of where you want to play.)\n"))
                if player_input not in range(1, 10):
                    print("Input has to be a number between 1 and 9.")
                    continue
                elif player_input in x_plays or player_input in l_plays:
                    print("Sorry that spot is taken.")
                    continue
                else:
                    break
            except ValueError:
                print("Input has to be a digit.")

        
        #  Get the x and y coordinates and update the table
        x,y = moves[player_input]
        game_table[x][y] = player
        tic_table.clear_rows()
        tic_table.add_rows(game_table)

        os.system('cls')
        if player == "X" :
            x_plays.append(player_input)  
            # Check for win
            if check_win(x_plays):
                print(tic_table)
                print("X wins")
                break
            player = "O"

        else:
            l_plays.append(player_input)
            game_table[x][y] = "O"
            # Check for win
            if check_win(l_plays):
                print(tic_table)
                print("O wins")
                break
            player = "X"

    print(tic_table)
    print("Draw")
        

while True:
    tic_tac_toe()
    play_again = input("Do you want to play again? (y/n): ").lower()
    if play_again != "y":
        break
