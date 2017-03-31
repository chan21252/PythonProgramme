# 生日快乐

birthdays = {'CC':'0625',
			'BB':'1230',
			'RJJ':'0830',
			'LT':'0921'	
			};

while True:
	print("请输入一个姓名(直接回车退出)：");
	name = input();
	if name == '':
		break;
		
	if name in birthdays:
		print(name + "的生日是" + birthdays[name]);
	else:
		print("我不知道" + name + "的生日");
		print("他/她的生日是？");
		baby = input();
		birthdays[name] = baby;
		print("生日数据库已经更新");