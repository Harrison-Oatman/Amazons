import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import matplotlib.animation as animation
import numpy as np

# used to color pieces based on their type
def color(num):
    return ['#000000','#ffffff','#c92014'][num]

# produes circle artist based on position
def make_circle(piece):
    return Circle((piece[0][0]+.5,piece[0][1]+.5),.3,color = color(piece[1]))

def visualize_game(position_lists,board_size=4):
    """
    produces a matplotlib animation to visualize a game
    -------------------------------------------------------------------
    args: game as a list of positions at each time, size of board
    out: returns None if successful in producing representation
    """
    # produce contourf of game board based on size parameter
    y = np.linspace(0,board_size,200,False)
    x = np.linspace(0,board_size,200,False)
    xy, yx = np.meshgrid(x,y)
    # floor function used to create grid
    grid = np.mod(np.floor(xy) + np.floor(yx),2)

    # produce figure for animation
    fig,ax = plt.subplots()

    # remove numbers and ticks for visual purposes
    ax.axis('equal')
    ax.tick_params(bottom=False,left=False,labelleft=False,labelbottom=False)

    # gameboard artist
    grid = ax.contourf(xy, yx, grid,2)

    # produce list of artists at each turn for artist animation
    circle_lists = []
    # iterate through turns
    for game_state in position_lists:
        current_circles = []
        # produce circle object for each piece
        for piece in posList:
            circle = ax.add_artist(make_circle(piece))
            current_circles.append(circle)
        # add turn to artist iterable
        circle_lists.append(current_circles)

    # animation function
    animation.ArtistAnimation(fig, circle_lists, interval=1000, repeat=True)
    plt.show()
    return None
