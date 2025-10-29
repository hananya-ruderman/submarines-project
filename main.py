from submarines.game_logic import init_game, is_won, is_lost, shoot
from submarines.user import print_status, print_end, parse_coords
from submarines.board import shots_left, count_remaining_ships

"""
1) choose_board_size
2) create_matrix + create_bool_matrix
3) 
"""
def play():
    # STATE CREATION
   
    state = init_game(6, 5, 10)

    while not is_lost(state) and not is_won(state):
        x, y = parse_coords(input("give me the coords"))
        print(x, y)
        shoot(state, x, y)
        shots_left(state["shots_left"])
        count_remaining_ships(state["ships"], state["shots"], state["n_ships"])
    
    print(print_status(state))
    print(print_end(state, True), is_won(state))

print(play())





    # ----> LOOP (While not did_win() and not did_lost())
    # ----> FINISH (WIN/LOOSE)




if __name__ == "__main__":
    play()