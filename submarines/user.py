from submarines.board import render_public, render_reveal


def choose_board_size():
    board_size = int(input("choose board size: "))
    return board_size

def parse_coords(raw: str, *, one_based: bool = True)->  tuple[int, int] | None:
    data = raw.split()
    if len(data) == 2:
        try:
            if int(data[0]) and int(data[1]):
                  return tuple(int(data))
        except Exception as e: 
                print("invalid input",e)                   

def print_status(state: dict)-> None:
    return f"shots_left{state["shots_left"]}, ships left{state["n_ships"]}, board state {render_public(state["ships"], state["shots"])}"

def print_end(state:dict, is_won)-> None:
    return f"board stotus {render_reveal(state["ships"], state["shots"])} {"won!!!" if is_won else "lost!!"}" 
     


if __name__ == "__main__":
    print()