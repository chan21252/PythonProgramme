#

def printBoard(board):
	print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R']);
	print('-+-+-');
	print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R']);
	print('-+-+-');
	print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R']);

theBoard = {'top-L':'', 'top-M':'', 'top-R':'',
			'mid-L':'', 'mid-M':'', 'mid-R':'',
			'low-L':'', 'low-M':'', 'low-R':''};

turn = 'X';

for i in range(9):
	printBoard(theBoard);
	print("现在是" + turn + "下棋,请选择下在哪个位置?");
	move = input();
	theBoard[move] = turn;

	if turn == 'X':
		turn = 'O';
	else:
		turn = 'X';

printBoard(theBoard);