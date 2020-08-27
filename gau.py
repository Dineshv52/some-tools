#-*-coding:utf-8-*-
import os
import time
import pyfiglet

def gau():
	ascii_banner = pyfiglet.figlet_format("gau scan")
	print(ascii_banner)
	print('开始运行gau外链扫描')
	url = input('请输入需要扫描的url：')
	os.system('echo -e "以下为gau外链扫描结果\n" >>report.txt')
	os.system('gau ' + url + ' >> report.txt')
	os.system('echo -e "\n\n\n" >>report.txt')
	print("扫描完成，请在report.txt中查看")

if os.path.isdir('go_tool/gau'):
	gau()
else:
	print('请在新窗口运行命令：\nwget https://github.com/lc/gau/releases/download/v1.0.3/gau_1.0.3_linux_amd64.tar.gz\ntar xvf gau_1.0.3_linux_amd64.tar.gz\nmv gau /usr/bin/gau')
	os.system('cd go_tool\ngnome-terminal')
	input("确定下载安装成功后请按回车键继续")
	gau()
