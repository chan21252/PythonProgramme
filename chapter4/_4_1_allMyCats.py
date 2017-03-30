# 序列

catName = [];

while True:
	print("输入第" + str(len(catName)+1) + "只猫的名字：");
	name = input();
	if name == '':
		break;
	catName = catName + [name];

print(catName);
print("猫的名字：");
for i in range(0,len(catName)):
	print(catName[i]);
