#! python3

heroRegex = re.compile(r'Batman|Tina Fey');

mo = heroRegex.search('Batman and Tina Fey');

mo.group();