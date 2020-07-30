"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    countOfX=0
    countOfO=0
    for row in board:
        for cell in row:
            if cell is X: countOfX+=1
            if cell is O: countOfO+=1

    return X if countOfX<=countOfO else O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    setOfActions=set()
    for i, row in enumerate(board):
        if EMPTY in row:
            for j, cell in enumerate(row):
                if cell is EMPTY:
                    setOfActions.add((i,j))
    return setOfActions

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    row, cell =action
    modified_board=copy.deepcopy(board)
    if modified_board[row][cell] is not None: 
        raise Exception
    modified_board[row][cell]=player(modified_board)
    return modified_board


def anyOfThreeRow(board,current_player):
    cp=current_player
    threeRow=[ board[0]==[cp,cp,cp], board[1]==[cp,cp,cp], board[2]==[cp,cp,cp] ]
    return any(threeRow)

def anyOfThreeCol(board,current_player):
    cp=current_player
    threeColumn=[ board[0][0]==cp and board[1][0]==cp and board[2][0]==cp,
    board[0][1]==cp and board[1][1]==cp and board[2][1]==cp,
    board[0][2]==cp and board[1][2]==cp and board[2][2]==cp]
    return any(threeColumn)

def anyOfTwoDiagonal(board,current_player):
    cp=current_player
    TwoDiagonal=[board[0][0]==cp and board[1][1]==cp and board[2][2]==cp,
    board[0][2]==cp and board[1][1]==cp and board[2][0]==cp ]
    return any(TwoDiagonal)

def winConditions(board,current_player):
    return any([anyOfTwoDiagonal(board,current_player), anyOfThreeCol(board,current_player), anyOfThreeRow(board,current_player)])

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if winConditions(board, X): return X
    if winConditions(board, O): return O
    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None: return True
    for row in board:
        if None in row:
            return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board):
        if winner(board)==X: return 1
        if winner(board)==O: return -1
        return 0

def minimaxValue(board,player,alpha,beta):
    if terminal(board):
        return utility(board)

    if player == X:
        v = -math.inf

        for action in actions(board):
            v = max(v, minimaxValue(result(board, action), O, alpha, beta))

            alpha = max(alpha,v)
            if alpha >= beta:
                break

    else:
        v = math.inf

        for action in actions(board):
            v = min(v, minimaxValue(result(board, action), X, alpha, beta))

            beta = min(beta,v)

            if alpha >= beta:
                break

    return v


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    alpha=-math.inf
    beta=math.inf

    optimalMove=None

    if player(board)==X:
        v = -math.inf

        for action in actions(board):
            modified_v = minimaxValue(result(board, action),O, alpha, beta)

            alpha = max(v, modified_v)

            if modified_v > v:
                v = modified_v
                optimalMove = action
                
    else:
        v = math.inf

        for action in actions(board):
            modified_v = minimaxValue(result(board, action), X, alpha, beta)

            beta = min(v, modified_v)

            if modified_v < v:
                v = modified_v
                optimalMove = action
    return optimalMove
