import numpy as np
import re
print(str(type(np.zeros((4,4),dtype='int8'))) == "<class 'numpy.ndarray'>")
print(np.zeros((4,4),dtype='int8').dtype == 'int8')
print(re.search('\(\(\d+, \d+\), [1-3]\)', str(((5,2),4))))

from Engine import Game

x = Game(4)
x.add_pieces([((0,0),1),((0,1),2),((1,1),1),((2,1),2),((3,1),1),((1,0),1)])
print(x.board.T)
print(x.find_valid_moves([(0,0)]))
