import os
import importlib.machinery


def main(poc, url):
	check = importlib.machinery.SourceFileLoader(poc, poc).load_module()
	return check.run(url)

fp = open("report.txt" , 'a+' , encoding="utf-8")
fp.write('以下为46POC扫描结果\n')
Plugins = "python_tool/46POC/plugins"
url = input("请输入需要扫描的url：")
for application in os.listdir(Plugins):
	file_path = os.path.join(Plugins, application)
	for path, dirs, file_poc in os.walk(file_path):
		for lists in file_poc:
			poc = f'{Plugins}/{application}/{lists}'
			if poc.endswith('.py'):
				result = main(poc, url)
				print(result)
				fp.write(str(result)+'\n')
fp.write('\n\n')
fp.close()
