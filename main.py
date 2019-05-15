import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import matplotlib.animation as animation
import numpy as np
import time

n = 4
y = np.linspace(0,n,200,False)
x = np.linspace(0,n,200,False)

xy, yx = np.meshgrid(x,y)
grid = np.mod(np.floor(xy) + np.floor(yx),2)

posLists = [[((0,0),0),((0,1),1),((1,0),2)],[((0,0),0),((0,1),1),((2,0),0)]]

def color(num):
    return ['#000000','#ffffff','#c92014'][num]

def make_circle(piece):
    return Circle((piece[0][0]+.5,piece[0][1]+.5),.3,color = color(piece[1]))

fig,ax = plt.subplots()

ax.axis('equal')
ax.tick_params(bottom=False,left=False,labelleft=False,labelbottom=False)

grid = ax.contourf(xy, yx, grid,2)

circleLists = []
for posList in posLists:
    circleList = []
    for piece in posList:
        circle = ax.add_artist(make_circle(piece))
        circleList.append(circle)

    # print(circleList)
    circleLists.append(circleList)

# print(circleLists)
anim = animation.ArtistAnimation(fig, circleLists, interval=1000, repeat=True)
plt.show()
