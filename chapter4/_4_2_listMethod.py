# 列表方法

spam = ['beijing',
		'shanghai',
		'guangdong',
		'jiangsu',
		'zhejiang'
		];

# 返回索引值
try:
	print(str(spam.index('jiangsu')));
	print(str(spam.index('sichuan')));
except Exception as ValueError:
	print("没有找到'sichuan'");

# 添加值到末尾
spam.append('sichuan');
print(spam);

# 插入
spam.insert(5, 'chongqing');
print(spam);

# 删除
try:
	spam.remove('zhejiang');
	print(spam);
	spam.remove('shandong');
	print(spam);
except Exception as ValueError:
	print("没有找到'shandong'，无法删除");

# 排序
spam.sort();	#正序
print(spam);

spam.sort(reverse=True);	#逆序
print(spam);

spam.append(56);
print(spam);
spam.sort();

try:
	spam.sort();
except Exception as TypeError:
	print("类型错误，无法排序");
