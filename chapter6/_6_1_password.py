#! python3
#

PASSWORDS = {
	'QQ': 'QWER123456',
	'weixin': 'qazwsx',
	'sinaweibo': '789456123aabbcc'
};

import sys, pyperclip

if len(sys.argv) < 2:
	print('Usage: python password.py [account] - copy account password');
	sys.exit();
	
account = sys.argv[1];

if account in PASSWORDS:
	pyperclip.copy(PASSWORDS[account]);
	print('Password for ' + account + ' copied to clipboard');
else:
	print('There is no account named ' + account);

input("Press <enter>");