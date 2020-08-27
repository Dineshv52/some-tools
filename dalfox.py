#-*-coding:utf-8-*-
import os
import time

def dalfox():
	url = input("请输入需要扫描的url：")
	string1 = '~/go/bin/dalfox url '+url+' -o report.txt'
	string2 = '~/go/bin/dalfox url '+url+' b https://hahwul.xss.ht -o report.txt'
	os.system('echo -e "以下为dalfox XSS漏洞扫描结果\n" >>report.txt')
	os.system(string1)
	os.system(string2)
	os.system('echo -e "\n\n\n" >>report.txt')
	print("扫描完成，请在report.txt中查看")

if os.path.exists('go_tool/dalfox'):
	dalfox()
else:
	print('请在新窗口运行命令：\ngit clone https://github.com/hahwul/dalfox\ncd dalfox\ngo install')
	time.sleep(2)
	os.system('cd go_tool\ngnome-terminal')
	input("确定下载安装成功后请按回车键继续")
	dalfox()
