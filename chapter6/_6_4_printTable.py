#! python3

'''
打印表格右对齐
apple	oranges	cherries	banana
Alice	Bob		Carol		David
dogs	cats	moose		goose
'''

'''
遍历二元列表
	在二元列表每一个元素的结尾加入制表符
	在每一行最后一个元素的结尾加入换行符
右对齐每一个元素
将每一个元素连接成字符串
打印字符串
'''
def prinTable(tableData):
	maxLength = 0;

	for i in range(len(tableData)):
		for j in range(len(tableData[i])):
			if len(tableData[i][j]) > maxLength:
				maxLength = len(tableData[i][j]);
			tableData[i][j] += '\t';
		tableData[i][j] += '\n';
	#print(str(maxLength));

	tableStr = '';
	
	for i in range(len(tableData)):
		for j in range(len(tableData[i])):
			tableStr += tableData[i][j].rjust(maxLength+1);

	print(tableStr);

tableData = [
	['apple', 'oranges', 'cherries', 'banana'],
	['Alice', 'Bob', 'Carol', 'David'],
	['dogs', 'cats', 'moose', 'goose']
];

prinTable(tableData);

'''输出结果
  apple         oranges        cherries         banana
  Alice             Bob           Carol          David
   dogs            cats           moose          goose

'''

