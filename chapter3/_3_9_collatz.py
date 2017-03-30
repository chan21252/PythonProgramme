# Collatz序列

import sys

def collatz(number):
	if number%2 == 0:
		number = number / 2;
	elif number%2 == 1:
		number = number * 3 + 1;
	return number;

print("请输入一个整数：");
try:
	num = int(input());	#用户输入
except ValueError:
	print("错误，输入非整数。");
	sys.exit();

while(num != 1):
	num = collatz(num);
	print(int(num));

