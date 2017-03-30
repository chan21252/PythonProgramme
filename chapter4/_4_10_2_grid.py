# 字符网络

# grid[0][0] = new[0][6]
grid = [['.', '.', '.', '.', '.', '.'],  
		['.', 'O', 'O', '.', '.', '.'],  
		['O', 'O', 'O', 'O', '.', '.'],  
		['O', 'O', 'O', 'O', 'O', '.'],  
		['.', 'O', 'O', 'O', 'O', 'O'],  
		['O', 'O', 'O', 'O', 'O', '.'],  
		['O', 'O', 'O', 'O', '.', '.'],  
		['.', 'O', 'O', '.', '.', '.'],  
		['.', '.', '.', '.', '.', '.']];

list_2d = [['0' for col in range(9)] for row in range(6)];

print(len(list_2d));
print(len(grid));

for y in range(len(grid)):
	for x in range(len(grid[y])):
		list_2d[y][x] =  grid[y][x];
		print(list_2d[y][x],end='');
	print();

print(grid);