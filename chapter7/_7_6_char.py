#! python3

'''
\d	0-9
\D	除了0-9以外的字符
\w 	字母、数字、下划线
\W 	除了字母、数字、下划线
\s  空格、制表符、换行符
\S  除了空格、制表符、换行符
[]	自定义字符集
^	开头必须匹配
$	结尾必须匹配
'''

import re;

xmasRegex = re.compile(r'\d+\s\w+');
mo = xmasRegex.findall('12 pigs, 11 dogs, 10 cats, 9 mouses');
print(mo);

#custom character set
helloRegex = re.compile(r'[hello]');
mo2 = helloRegex.findall('lol my name is herry');
print(mo2);

#^ and $
beginWithHello = re.compile(r'^Hello');
mo3 = beginWithHello.search('HelloWorld');
print(mo3.group());

mo31 = beginWithHello.search('I will say Hello!');
if None == mo31:
	print('None');

endWithNum = re.compile(r'\d$');
mo4 = endWithNum.search('Your age is 18');
print(mo4.group());

#.
atRegex = re.compile(r'.at');
mo5 = atRegex.findall('The cat in the hat sat on the flat mat.');
print(mo5);
