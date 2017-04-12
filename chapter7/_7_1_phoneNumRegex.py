#! python3

'''
1．用import re 导入正则表达式模块。
2．用re.compile()函数创建一个Regex 对象（记得使用原始字符串）。
3．向Regex 对象的search()方法传入想查找的字符串。它返回一个Match 对象。
4．调用Match 对象的group()方法，返回实际匹配文本的字符串。
'''

import re

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)');

mo = phoneNumRegex.search("我的电话号码是415-555-6757。");

print("识别电话号码是" + mo.group(1) + "-" + mo.group(2));

areaCode, mainNumber = mo.groups();
print("区号是" + areaCode + ",号码是" + mainNumber);

