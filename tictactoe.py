# string --> list
def from_string_in_list(field):
    return [list(field[:3]), list(field[3:6]), list(field[6:])]


# Outputting field
def field_output(field):
    print("---------")
    print('|', field[0][0], field[0][1], field[0][2], '|')
    print('|', field[1][0], field[1][1], field[1][2], '|')
    print('|', field[2][0], field[2][1], field[2][2], '|')
    print("---------")


# User's entering
def user_input():
    string = ''
    while len(string) != 9:
        string = input().upper()
    return string


# Enter coordinates
def enter_coordinate(field):
    coordinate = []
    while not coordinate:
        x, y = input('Enter the coordinates: ').split()
        if not x.isdigit() and not y.isdigit():
            print('You should enter numbers!')
        elif (int(x) or int(y)) < 1 or (int(x) or int(y)) > 3:
            print('Coordinates should be from 1 to 3!')
        elif field[int(x) - 1][int(y) - 1] in ('X', 'O'):
            print('This cell is occupied! Choose another one!')
        else:
            coordinate = [int(x) - 1, int(y) - 1]
    return coordinate


# Entering 'X' in the field
def entering_in_field(battlefield, xy, char):
    battlefield[xy[0]][xy[1]] = char
    return battlefield


# Checking the coincidence of combinations
def entry_indexes(battlefield, char):
    ind = [[i, j] for i in range(3) for j in range(3)]
    combo_ind = [ind[:3], ind[3:6], ind[:6], ind[::3], ind[1::3], ind[2::3], ind[::4], ind[2:7:2]]
    if char == 'X' or char == 'O':
        coordinates = char_indexes(battlefield, char)
        for combo in combo_ind:
            if all([indexes in coordinates for indexes in combo]):
                return True
    else:
        if any([char in battlefield[i] for i in range(3)]):
            return True


# Entering indexes
def char_indexes(battlefield, char):
    coordinates = []
    for i in range(3):
        for j in range(3):
            if battlefield[i][j] == char:
                coordinates.append([i, j])
    return coordinates


# Checking game status
def checking(battlefield):
    if entry_indexes(battlefield, 'O'):
        return "O wins"
    elif entry_indexes(battlefield, 'X'):
        return "X wins"
    elif not entry_indexes(battlefield, '_'):
        return "Draw"
    else:
        return False


# begin
USERS = ['X', 'O']
string_field = '_' * 9
list_field = from_string_in_list(string_field)
field_output(list_field)
check = False
while not check:
    for i in range(2):
        coordinates = enter_coordinate(list_field)
        list_field = entering_in_field(list_field, coordinates, USERS[i])
        field_output(list_field)
        check = checking(list_field)
        if check:
            break
print(check)
