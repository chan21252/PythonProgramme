# 异常处理2

def spam(divideBy):
	return 42 / divideBy;

try:
	print(spam(5));
	print(spam(6));
	print(spam(0));
	print(spam(1));
except ZeroDivisionError:
	print("Error: Invalid argument.");