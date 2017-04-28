#! python3

# 强口令检测

import re;

def passwordCheck(password):
	status = False;
	if len(password) >= 8:
		upperRegex = re.compile(r'[A-Z]');
		lowerRegex = re.compile(r'[a-z]');
		numRegex = re.compile(r'[0-9]');

		'''
		print(upperRegex.search(password).group());
		print(lowerRegex.search(password).group());
		print(numRegex.search(password).group());
		'''

		if None != upperRegex.search(password):
			if None != lowerRegex.search(password):
				if None != numRegex.search(password):
					print('密码符合要求');
					status = True;
				else:
					print('必须包含至少一位数字');
			else:
				print('必须包含小写字母');
		else:
			print('必须包含大写字母');
	else:
		print('必须超过8个字符');
		status = False;

	return status;

pw = input();

while (passwordCheck(pw) == False):
	pw = input();
