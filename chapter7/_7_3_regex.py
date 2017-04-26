#! Python3

#

import re;

# ?匹配
questionRegex = re.compile(r'(wo)?man');

mo = questionRegex.search('I am a man.');
mo2 = questionRegex.search('I am a woman.');

print(mo.group());
print(mo2.group());

# *匹配
asteriskRegex = re.compile(r'(c)*han');

mo3 = asteriskRegex.search('I am ccccccccccchan');
mo4 = asteriskRegex.search('I am han');

print(mo3.group());
print(mo4.group());

# +匹配

plusRegex = re.compile(r'(c)+han');

mo5 = plusRegex.search('I am ccccccccccchan');
mo6 = plusRegex.search('I am han');

print(mo5.group());
print(mo6);

# {}匹配

braceRegex = re.compile(r'(ha){3}');
braceRegex2 = re.compile(r'(ha){0,5}');

mo7 = braceRegex.search('hahahahahaha');

print(mo7.group());


'''
?	匹配0或1次
*	匹配0或多次
+	匹配1或多次
{}	匹配特定次数
	{n}		匹配n次
	{n,}	匹配>=n次
	{,n}	匹配<=n次
	{n1,n2}	匹配>=n1&&<=n2次
默认贪心的匹配，即取最长匹配的表达式
非贪心的匹配{n1,n2}?
'''