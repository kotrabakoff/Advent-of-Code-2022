round = input()
total_score = 0

while round:
    both = round.split(" ")
    opponents_move = both[0]
    my_move = both[1]
    if opponents_move == "A":#rock
        if my_move == "X":#rock
            total_score += 3 + 1
        elif my_move == "Y":#paper
            total_score += 6 + 2
        else:#scissor
            total_score += 0 + 3
    elif opponents_move == "B":#paper
        if my_move == "X":#rock
            total_score += 0 + 1
        elif my_move == "Y":#paper
            total_score += 3 + 2
        else:#scissor
            total_score += 6 + 3
    elif opponents_move == "C":#scissor
        if my_move == "X":#rock
            total_score += 6 + 1
        elif my_move == "Y":#paper
            total_score += 0 + 2
        else:#scissor
            total_score += 3 + 3
    print(total_score)
    round = input()