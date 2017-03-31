# 字符网络

# [0][0] [1][0] [2][0] [3][0] ……共 9 列
# [0][1] [1][1] [2][1] [3][1] ……
# ……
# 共 6 行

grid = [['.', '.', '.', '.', '.', '.'],  
		['.', 'O', 'O', '.', '.', '.'],  
		['O', 'O', 'O', 'O', '.', '.'],  
		['O', 'O', 'O', 'O', 'O', '.'],  
		['.', 'O', 'O', 'O', 'O', 'O'],  
		['O', 'O', 'O', 'O', 'O', '.'],  
		['O', 'O', 'O', 'O', '.', '.'],  
		['.', 'O', 'O', '.', '.', '.'],  
		['.', '.', '.', '.', '.', '.']];

# list_2d = [['0' for col in range(9)] for row in range(6)];
# print(len(list_2d));
# print(len(grid));

for y in range(len(grid)):
	for x in range(len(grid[y])):
		print(grid[y][x],end='');
	print('');

print('===============');

for cols in range(len(grid[0])):
	for rows in range(len(grid)):
		print(grid[rows][cols],end='');
	print('');
