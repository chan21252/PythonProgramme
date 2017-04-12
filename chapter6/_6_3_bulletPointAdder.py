#! python3
# 将'*'添加到无序列表每一项的前面

import pyperclip

text = pyperclip.paste();
print(text);

lines = [];
if '\n' in text:
	lines = text.split('\n');
elif '\r' in text:
	lines = text.split('\r');
print(lines);

for i in range(len(lines)):
	lines[i] = "* " + lines[i];
print(lines);

text = '\n'.join(lines);
print(text);

pyperclip.copy(text);

