#! python

#findall

import re;

phoneNumerRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d');
mo = phoneNumerRegex.findall('cell:415-555-9999 work:212-555-0000');
print(mo);

phoneNumerRegex2 = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)');
mo2 = phoneNumerRegex2.findall('cell:415-555-9999 work:212-555-0000');
print(mo2);
	