def spam(divideBy):
	try:
		return 42 / divideBy;
	except ZeroDivisionError:
		print("Error: Invalid argument.", end="0");

print(spam(2));
print(spam(6));
print(spam(0));