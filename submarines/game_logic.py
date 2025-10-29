from submarines.board import create_matrix, create_bool_matrix
from submarines.user import choose_board_size


def init_game(size: int, n_ships: int, max_shots: int)-> dict:
    state = { 
        "size": size, 
        "ships": create_matrix(6, 0), 
        "shots": create_bool_matrix(6, False), 
        "n_ships": n_ships, 
        "max_shots": max_shots, 
        "shots_left": max_shots 
    }
    return state



def shoot(state: dict, x: int, y:int)->  tuple[bool, str]:
    if x <= state["size"] and y <= state["size"] and state["shots_left"] and not state["shots"][x][y]:
       state["shots_left"] -= 1
       if state["ships"][x][y] == 1:
            state["n_ships"] -= 1
            return
    else:
        print("not valid shot") 

def is_won(state: dict)-> bool:
    return True if state["n_ships"] == 0 else False 


def is_lost(state: dict)-> bool:
    if state["shots_left"] == 0 and state["n_ships"] > 0:
        return True
    

if __name__ == "__main__":  
    print(init_game(5, 5, 5))    
    
        
         