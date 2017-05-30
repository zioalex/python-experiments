#!/usr/bin/python3

PRINCESS = 'p'
BOT = 'm'
instructions = []


def displayPathtoPrincess(n, grid):
    ''' find the princess '''
    for m in range(0, n):
        if PRINCESS in grid[m]:
            princess_position = (m, grid[m].index(PRINCESS))
    print('the pricess is here:', princess_position)
    for m in range(0, n):
        if BOT in grid[m]:
            bot_position = (m, grid[m].index(BOT))
    print('the bot is here:', bot_position)

    new_bot_position = bot_position
    while True:
        if new_bot_position[0] < princess_position[0]:
            print("DOWN")
            new_bot_position = (new_bot_position[0] + 1, new_bot_position[1])
        elif new_bot_position[0] > princess_position[0]:
            print("UP")
            new_bot_position = (new_bot_position[0] - 1, new_bot_position[1])
        if new_bot_position[1] < princess_position[1]:
            print("RIGHT")
            new_bot_position = (new_bot_position[0], new_bot_position[1] + 1)
        elif new_bot_position[1] > princess_position[1]:
            print("LEFT")
            new_bot_position = (new_bot_position[0], new_bot_position[1] - 1)
        if new_bot_position == princess_position:
            print("The princess is here %s and now also the bot is here %s"
                  % (princess_position, new_bot_position))
            break


def displayPathtoPrincess_singleline(array_lenght, index, __input_line, bot_position, princess_position):
    ''' find the princess '''
    if princess_position is None:
        if PRINCESS in __input_line:
            princess_position = (index, __input_line.index(PRINCESS))
        # print('the pricess is here:', princess_position)
    if bot_position is None:
        if BOT in __input_line:
            bot_position = (index, __input_line.index(BOT))
        # print('the bot is here:', bot_position)

    new_bot_position = bot_position
    # if new_bot_position is not None and princess_position is not None:
    if (array_lenght - 1) == index:
        while new_bot_position != princess_position:
            if new_bot_position[0] < princess_position[0]:
                print("DOWN")
                new_bot_position = (new_bot_position[0] + 1, new_bot_position[1])
            elif new_bot_position[0] > princess_position[0]:
                print("UP")
                new_bot_position = (new_bot_position[0] - 1, new_bot_position[1])
            if new_bot_position[1] < princess_position[1]:
                print("RIGHT")
                new_bot_position = (new_bot_position[0], new_bot_position[1] + 1)
            elif new_bot_position[1] > princess_position[1]:
                print("LEFT")
                new_bot_position = (new_bot_position[0], new_bot_position[1] - 1)
            # if new_bot_position == princess_position:
            #    print("The princess is here %s and now also the bot is here %s"
            #          % (princess_position, new_bot_position))
    return new_bot_position, princess_position

m = int(input())
#grid = [["-" for x in range(m)] for y in range(m)]
#for x in range(0, m):
#    for y in range(0, m):
#        grid[x][y] = input().strip()
bot_pos = None
prin_pos = None
for x in range(0, m):
    input_list = list(input().strip())
    bot_pos, prin_pos = displayPathtoPrincess_singleline(m, x, input_list, bot_pos, prin_pos)
    
#for x in range(0, m):
#    print(grid[x]),

#displayPathtoPrincess(m, grid)
