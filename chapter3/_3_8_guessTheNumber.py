# 猜数字

import random

# 生产随机数
secretNumber = random.randint(1,20);
print("这是一个1~20之间的数字。");

# 猜6次
for i in range(1,7):
	print("开始猜：");
	guess = int(input());

	if guess < secretNumber:
		print("猜小了。");
	elif guess > secretNumber:
		print("猜大了。");
	else:
		break; # 猜对了就跳出循环

if guess == secretNumber:
	print("你猜了" + str(i) + "次猜中了");
else:
	print("对不起，你猜了6次没猜中，正确数字是" + str(secretNumber));