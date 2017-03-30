# 字符串和列表

spam = 'koala is a dog';

try:
	spam[0] = 's'; 
except Exception as TypeError:
	print("类型错误，str不支持重新赋值");

newSpam = spam[0:9] + 'not' + spam[8:14];

print(newSpam);