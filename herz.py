grid = [['.','.','.','.','.','.'],
	['.','0','0','.','.','.'],
	['0','0','0','0','.','.'],
	['0','0','0','0','0','.'],
	['.','0','0','0','0','0'],
	['0','0','0','0','0','.'],
	['0','0','0','0','.','.'],
	['.','0','0','.','.','.'],
	['.','.','.','.','.','.']]

for y in range(0,6,1):
	for x in range(0,9,1):
		print(grid[x][y],end="")
	print("")
