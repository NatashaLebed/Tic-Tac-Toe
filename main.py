def get_coordinates():
    while True:
        coordinates = input('Enter the coordinates:')
        if not coordinates[0].isdigit() or not coordinates[2].isdigit():  # check digit input
            print('You should enter numbers!')
            continue
        x, y = int(coordinates[0]), int(coordinates[2])
        if not (1 <= x <= 3) or not (1 <= y <= 3):  # check x, y are from 1 to 3
            print('Coordinates should be from 1 to 3!')
            continue
        if grid[x - 1][y - 1] != ' ':  # check is this cell occupied
            print('This cell is occupied! Choose another one!')
            continue
        return x - 1, y - 1


def winner(symbol):
    # horizontal win check
    for i in range(3):
        if grid[i].count(symbol) == 3:
            return True

    # vertical win check
    for i in range(3):
        vertical_line = [grid[j][i] for j in range(3)]
        if vertical_line.count(symbol) == 3:
            return True

    # diagonal win check
    diagonal_line_1 = [grid[i][i] for i in range(3)]
    diagonal_line_2 = [grid[i][2 - i] for i in range(3)]
    if diagonal_line_1.count(symbol) == 3 or diagonal_line_2.count(symbol) == 3:
        return True


def print_grid():
    print('---------')
    print('| {} {} {} |'.format(grid[0][0], grid[0][1], grid[0][2]))
    print('| {} {} {} |'.format(grid[1][0], grid[1][1], grid[1][2]))
    print('| {} {} {} |'.format(grid[2][0], grid[2][1], grid[2][2]))
    print('---------')


grid = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
print_grid()
moves = 0

while True:
    x, y = get_coordinates()
    moves += 1
    grid[x][y] = 'O' if moves % 2 == 0 else 'X'
    print_grid()

    # check winners or Draw
    if winner('X'):
        print('X wins')
        break
    elif winner('O'):
        print('O wins')
        break
    elif moves == 9:
        print('Draw')
        break
