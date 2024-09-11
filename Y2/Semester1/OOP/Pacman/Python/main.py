import curses
import time
from Assets import Assets

def show_grid(stdscr, grid):
    # Initialize curses and set up colors
    curses.start_color()

    # Use extended 256 color range if supported
    curses.use_default_colors()
    
    curses.init_pair(1, 226, -1)  # Yellow (from 256 color palette)
    curses.init_pair(2, 196, -1)  # Red (from 256 color palette)
    curses.init_pair(3, 21, -1)   # Blue (from 256 color palette)

    for row in grid:
        for cell in row:
            if cell == Assets.PACMAN:  # PACMAN
                stdscr.addstr(f"{cell} ", curses.color_pair(1))
            elif cell ==  Assets.GHOST:  # GHOST
                stdscr.addstr(f"{cell} ", curses.color_pair(2))
            elif cell == Assets.WALL:  # WALL
                stdscr.addstr(f"{cell} ", curses.color_pair(3))
            else:
                stdscr.addstr(f"{cell} ")
        stdscr.addstr("\n")


def init_grid(grid_height=9, grid_width = 30):

    HEIGHT = min(max(9,grid_height), 15) 
    WIDTH = min(max(grid_width, 30), 35)

    #  Ensure odd height and width for ideal centering
    if HEIGHT % 2 != 1:
        HEIGHT += 1
    if WIDTH % 2 != 1:
        WIDTH +=1


    grid = [[Assets.FOOD for _ in range(WIDTH)] for _ in range(HEIGHT)]

    for i in range(WIDTH):
        grid[0][i] = Assets.WALL
        grid[HEIGHT - 1][i] = Assets.WALL


    for i in range(HEIGHT):
        grid[i][0] = Assets.WALL
        grid[i][WIDTH - 1] = Assets.WALL

    # 5 x 23 art
    art = [
        ['▀','▀','▀','•','▀','▀','▀','•','▀','▀','•','•','▀','▀','•','•','•','▀','•','•','▀','▀',"•"],
        ['▀','•','•','•','▀','•','•','•','•','•','▀','•','•','▀','•','•','▀',' ','▀','•','•','▀',"•"],
        ['▀','•','•','•','▀','▀','▀','•','•','•','▀','•','•','▀','•','•','▀',' ','▀','•','•','▀',"•"],
        ['▀','•','•','•','•','•','▀','•','▀','•','•','•','•','▀','•','•','▀',' ','▀','•','•','▀',"•"],
        ['▀','▀','▀','•','▀','▀','▀','•','▀','▀','▀','•','▀','▀','▀','•','•','▀','•','•','▀','▀','▀'],
    ]

    
    start_x = (HEIGHT - 5) // 2 # starting x for the art
    start_y = (WIDTH - 23) // 2 # starting y for the art

    for i in range(len(art)):  # Loop over rows of art
        for j in range(len(art[i])):  # Loop over columns of each row
            grid[start_x + i][start_y + j] = art[i][j]

    grid[HEIGHT // 2][1] = Assets.PACMAN
    grid[HEIGHT // 2][-2] = Assets.GHOST

    return grid, HEIGHT, WIDTH

def move_pacman(stdscr):
    curses.curs_set(0)  # Hide the cursor
    stdscr.nodelay(1)   # Don't block waiting for input

    grid, HEIGHT, WIDTH = init_grid()
    pacman_x = 3
    pacman_y = 3

    grid[pacman_y][pacman_x] = 'P'
    direction = None

    while True:
        key = stdscr.getch()

        if key == curses.KEY_UP:
            direction = 'up'
        elif key == curses.KEY_DOWN:
            direction = 'down'
        elif key == curses.KEY_LEFT:
            direction = 'left'
        elif key == curses.KEY_RIGHT:
            direction = 'right'

        # Update Pac-Man's position based on the direction
        if direction == 'up' and grid[pacman_y - 1][pacman_x] != Assets.WALL:
            pacman_y -= 1
        elif direction == 'down' and grid[pacman_y + 1][pacman_x] != Assets.WALL:
            pacman_y += 1
        elif direction == 'left' and grid[pacman_y][pacman_x - 1] != Assets.WALL:
            pacman_x -= 1
        elif direction == 'right' and grid[pacman_y][pacman_x + 1] != Assets.WALL:
            pacman_x += 1

        # Clear old position
        for y in range(HEIGHT):
            for x in range(WIDTH):
                if grid[y][x] == Assets.PACMAN:
                    grid[y][x] = Assets.EMPTY

        # Set new position
        grid[pacman_y][pacman_x] = Assets.PACMAN

        stdscr.clear()
        show_grid(stdscr, grid)
        stdscr.refresh()

        time.sleep(0.2)  # Control the movement speed


# Run the curses main loop
curses.wrapper(move_pacman)
