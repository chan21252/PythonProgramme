# continue and break

while True:
	print('what is your name?');
	name = input();

	if name != 'chan':
		continue;

	print('Hello,chan!');
	print('what is password?');

	password = input();

	if password == 'fish':
		break;

print('Access granted.');