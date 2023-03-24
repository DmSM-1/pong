import curses
from time import sleep

begin_x = 0; begin_y = 0
height = 40; width = 60 
fps = 2


stdscr = curses.initscr()
curses.curs_set(False)
curses.start_color()
curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLUE)
win = curses.newwin(height+1, width+1, begin_y, begin_x)

def border(win):
    global begin_x, begin_y, height, width
    for i in range(width):
        win.addch(0, i, '█', curses.color_pair(1))
        win.addch(height-1, i, '█', curses.color_pair(1))
    for i in range(height):
        win.addch(i, 0, '█', curses.color_pair(1))
        win.addch(i, width-1, '█', curses.color_pair(1))


border(win)
win.refresh()
vect = [1,1]
position = [height//2, width//2]

while ...:
    win.addch(position[0], position[1], '●')
    if position[0] in [1, height-2]:
        vect[0] *= -1
    if position[1] in [1, width-2]:
        vect[1] *= -1
    win.refresh()
    win.addch(position[0], position[1], ' ')
    position[0]+=vect[0]
    position[1]+=vect[1]
    sleep(1/fps)



#curses.noecho()
#curses.cbreak()
#
#curses.nocbreak()
#curses.echo()

curses.endwin()