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