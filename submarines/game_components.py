import random

def submarines_amount_and_positions(board_size:int) -> list[list[int, int]]:

    placed = []
    placed = set(placed)
    submarines_amount = random.randint(1, board_size*board_size)
    while len(placed) < submarines_amount:
        chek_len = len(placed)
        row = random.randint(0, board_size - 1)
        col = random.randint(0, board_size - 1)
        placed.add((row, col))
        if len(placed) == chek_len:
            submarines_amount += 1

    return placed, submarines_amount


def shots_amount(submarines_amount):
    submarines_amount = submarines_amount_and_positions()[1]
    shots = random.randint(submarines_amount+3, )
    
    return shots

if __name__ == "__main__":
    print(submarines_amount_and_positions(6))
    print(shots_amount(6))
