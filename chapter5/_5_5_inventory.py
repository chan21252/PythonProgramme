#! python3
# inventory.py

# 显示物品栏
def displayInventor(inventory):
	print('物品清单:');
	totalItems = 0;
	for i,j in inventory.items():	#遍历inventory,返回键-值元组
		print(str(j) + '\t' + i);
		totalItems += j;
	print("物品总数:" + str(totalItems));

''' 
添加掉落物到物品栏
遍历loot
loot的值在 inventory 中没有的，inventory添加该key
loot的值在 inventory 中已有的，inventory对应key的value +1
'''
def addToInventory(inventory, loot):
	for items in loot:
		inventory.setdefault(items, 0);
		inventory[items] += 1;
	return inventory;

# 当前物品栏
stuff = {
	'装备': 12,
	'宝石': 28,
	'图纸': 5,
	'金币': 1000
};

displayInventor(stuff);		

dragonLoot = ['金币', '装备', '金币', '徽章', '徽章', '荣誉'];

stuff = addToInventory(stuff, dragonLoot);

displayInventor(stuff);

input("Press <enter>")