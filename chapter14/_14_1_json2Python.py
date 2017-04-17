#! python3

import json;

jsonData = '{"items":[{"ies_id":"pengpai_5mc","plt":"MOBILE","impression":0,"click":1398},{"ies_id":"pengpai_5mc","plt":"PC","impression":0,"click":3}],"media_id":"澎湃","hour":"11","date":"20170417","items_size":2}';

jsonDataAsPythonValue = json.loads(jsonData);

print(str(jsonDataAsPythonValue));

for i in jsonDataAsPythonValue.items():
	print(i);

print(str(len(jsonDataAsPythonValue)));