import numpy as np
import re

class Game:
    """
    This class represents the game engine itself, and its methods are
    how we interact with the game
    """

    def __init__(self, board_size = 4,board = None):
        if board is None:
            self.board = np.zeros((board_size,board_size),dtype='int8')
        elif str(type(board)) == "<class 'numpy.ndarray'>":
            if board.dtype == 'int8' and board.min >= 0 and board.max <= 3:
                self.board = board
            else:
                raise ValueError('board must be ndarray of type int8 with values 0-3')
        else:
            raise ValueError('board must be ndarray')
        self.board_size = board_size
        self.turn = 0
        self.active = True

    def add_pieces(self, piece_list):
        """
        adds a list of pieces to a game at positions specified
        --------------------------------------------------------
        args: list of positions and teams of pieces to be added
        out: return True if pieces have been successfully added
        """
        success = True
        for piece in piece_list:
            if not self.add_piece(piece):
                print(f'Warning: piece at {piece[0]} not added - space occupied')
                success = False
        return success

    def add_piece(self, piece):
        """
        helper function to add individual pieces
        -----------------------------------------
        args: piece ((x pos, y pos), piece 1-3)
        """
        if re.search('\(\(\d+, \d+\), [1-3]\)', str(piece)) == None:
            raise Exception('Player format: ((x pos, y pos),piece 1-3)')

        if (
          not 0 <= piece[0][0] < self.board_size) or (
          not 0 <= piece[0][1] < self.board_size):
            raise Exception('Piece index out of range')

        if self.board[piece[0][0]][piece[0][1]] == 0:
            self.board[piece[0][0]][piece[0][1]] = piece[1]
            return True

        return False

    def find_valid_moves(self, piece_location, is_arrow = False):
        """
        Twice recursive function determining the valid moves for a piece
        -----------------------------------------------------------------
        Args: location of the piece being moved, if the piece is an arrow
        Out: list of moves [(startpos),(endpos),(arrowpos)], or None if no exist
        """
        self.temp_board = self.board.copy()
        self.temp_board[piece_location[0][0]][piece_location[0][1]] = 0
        moves_list = []
        for direction in [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]:
            current_loc = piece_location[-1]
            x = current_loc[0] + direction[0]
            y = current_loc[1] + direction[1]
            while (0 <= x < self.board_size and
                   0 <= y < self.board_size and
                   self.temp_board[x][y] == 0):
                if is_arrow:
                    moves_list.append([piece_location[0],piece_location[1],(x,y)])
                else:
                    moves_list.extend(self.find_valid_moves([piece_location[0],
                                                      (x,y)],is_arrow = True))
                x += direction[0]
                y += direction[1]
        if moves_list != []:
            return moves_list
        else:
            return None
