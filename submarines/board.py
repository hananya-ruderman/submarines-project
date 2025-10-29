

def create_matrix(size: int = 6 , fill: int = 0)-> list[list[int]]:
    return [[fill for j in range (size)] for i in range(size)]
   
def create_bool_matrix(size: int  = 6 ,fill: bool = False)-> list[list[bool]]:
    return [[fill for j in range (size)] for i in range (size)]

def shots_left(state: dict):
    shots_for_using -= 1
    return shots_for_using

     
def in_bounds(size:int, x: int, y: int)-> bool:

     if x <= size and y <= size:
          return True
     else:
          return False
     
def count_remaining_ships(ships: list[list[int]], shots: list[list[bool]])-> int:
    ships_left = 0
    for i in range(len(ships)):
         for j in range(len(ships)):
              if ships[i][j] == 1 and shots[i][j] == False:
                   ships_left += 1
    return ships_left

def render_public(ships: list[list[int]], shots: list[list[bool]])-> str:
    the_board_status = ""
    for x in range(len(ships)):
        for y in range(len(ships)):
            if ships[x][y] == 1 and shots[x][y]== True:
                the_board_status += f"ships [{x}, {y}] = v, "
            elif ships[x][y] == 0 and shots[x][y]== True:
                  the_board_status += f"ships [{x}, {y}] = x, "
            elif shots[x][y]== False:
                  the_board_status += f"ships [{x}, {y}] = O, "
                 
    return the_board_status

def render_reveal(ships: list[list[int]], shots: list[list[bool]])-> str:
    submarines = ""
    for x in range(len(ships)):
        for y in range(len(ships)):
              if ships[x][y] == 1 and  shots[x][y]== False:
                   submarines += f"ships [{x}, {y}] = 1, "
    return submarines
             
    
    
    





if __name__ == "__main__":
     print(create_matrix(0,0))
     print(create_bool_matrix(5, False))
     print(in_bounds(5, 4, 5))
     print(count_remaining_ships([[1,1], [1,0]], [[True,True],[True,True]]))
     print(render_public(create_matrix(5, 1), create_bool_matrix(5, True)))
     print(render_reveal(create_matrix(5, 1), create_bool_matrix(5, False)))

    
    