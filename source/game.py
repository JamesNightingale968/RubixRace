import numpy as np
import random

def init_random_board():
	board = np.zeros((5,5), dtype=int)
	tiles = [1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,0]
	random.shuffle(tiles)
	for i in range(board.shape[0]):
		for j in range(board.shape[1]):
			board[i,j]=tiles.pop()
	return board

def init_pattern():
	board = np.zeros((3,3), dtype=int)
	tiles = [1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,]
	random.shuffle(tiles)
	for i in range(board.shape[0]):
		for j in range(board.shape[1]):
			board[i,j]=tiles.pop()
	return board

print(init_random_board())
print(init_pattern())
