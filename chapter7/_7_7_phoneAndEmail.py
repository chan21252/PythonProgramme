#! python3

'''
功能：电话号码和e-mail地址提取
时间：2017-04-26
'''

'''
1.从剪贴板中获得文本
2.找出文本中的电话号码和e-mail地址
3.把他们粘贴到剪贴板

1.pyperclip模块复制和粘贴字符串
2.建立电话号码和e-mail的正则表达式
3.在字符串中找到正则表达式的所有匹配
4.整理匹配到的字符串
5.输出到剪贴板
'''

import re, pyperclip;

# 电话号码正则表达式
phoneRegex = re.compile(r'''(
	(\d{3})						#区号
	(\s|-|\.)?					#分隔符
	(\d{3})						#号码段1
	(\s|-|\.)?					#分隔符
	(\d{4})						#号码段2
	)''',re.VERBOSE);

# email正则表达式
emailRegex = re.compile(r'''(
	[a-zA-Z0-9._%+-]+			#用户名
	@							#@
	[a-zA-Z0-9._-]+				#域名
	(\.[a-zA-Z]{2,4})			#.com/cn
	)''',re.VERBOSE);

# 获取剪贴板的文本
text = str(pyperclip.paste());
matches = [];

# 匹配电话号码
for group in phoneRegex.findall(text):
	phoneNum = '-'.join([group[1],group[3],group[5]]);
	matches.append(phoneNum);

# 匹配e-mail
for group2 in emailRegex.findall(text):
	matches.append(group2[0]);

print(matches);

# 输出结果
if len(matches) > 0:
	pyperclip.copy('\n'.join(matches));
	print('匹配结果如下:');
	print('\n'.join(matches));
else:
	print('没有匹配结果.');

'''
Contact Us

No Starch Press, Inc.
245 8th Street
San Francisco, CA 94103 USA
Phone: 800.420.7240 or +1 415.863.9900 (9 a.m. to 5 p.m., M-F, PST)
Fax: +1 415.863.9950

Reach Us by Email

General inquiries: info@nostarch.com
Media requests: media@nostarch.com
Academic requests: academic@nostarch.com (Please see this page for academic review requests)
Help with your order: info@nostarch.com
Reach Us on Social Media

Twitter
Facebook
'''

'''
['800-420-7240', '415-863-9900', '415-863-9950', 'info@nostarch.com', 'media@nostarch.com', 'academic@nostarch.com', 'info@nostarch.com']
匹配结果如下:
800-420-7240
415-863-9900
415-863-9950
info@nostarch.com
media@nostarch.com
academic@nostarch.com
info@nostarch.com
'''

