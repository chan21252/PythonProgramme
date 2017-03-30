# 逗号代码

# 为列表赋值
# 取出最后一个值
# 在最后一个值前面加上'and'
# 返回新的列表

def insertAnd(list):
	list[-1] = 'and ' + list[-1];
	return list;


spam = ['apples', 'bananas', 'tofu', 'cats'];
spam = insertAnd(spam);
print(spam);