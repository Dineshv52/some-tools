#-*-coding:utf-8-*-
import os
import pyfiglet
import time

print("请先下载安装go环境\n#下载go\nhttps://studygolang.com/dl\n#解压\ntar -xzf go1.15.linux-amd64.tar.gz -C /usr/local\n#加环境变量(export PATH=$PATH:/usr/local/go/bin)\ngedit /etc/profile\nsource /etc/profile\ngedit /home/.bashrc\n重开terminal窗口\n#安装成功\ngo version\n#设置国内代理\ngo env -w GOPROXY=https://goproxy.cn\n")
input('确认安装成功后请按回车键继续')
print('***********************************')
os.system('go version')

print("如运行失败请清除此目录")

i=1
while True:
	print("1.常规扫描工具(信息收集)\n2.漏洞扫描工具(探测&利用)\n3.连接工具\n4.暴力破解\n5.密码工具\n6.社会工程学工具\n7.其他工具\n")
	print("执行工具次数 "+str(i)+" 次")
	tool=input("请选择执行工具：")
	if tool == '1':
		ascii_banner = pyfiglet.figlet_format("simple scan")
		print(ascii_banner)
		print("常规扫描工具(信息收集)")
		print("1.外链扫描(gau)\n2.端口扫描(nmap)")
		num = input("请输入执行的扫描工具：")
		if num == '1':
			print("开始运行扫描工具")
			os.system('python3 gau.py')
			i=i+1
		if num == '2':
			ip = input("请输入需要扫描的ip(可为ip段)：")
			exp = 'nmap --reason -A '+ip+' -oN report.txt'
			os.system(exp)
			i=i+1
	if tool == '2':
		ascii_banner = pyfiglet.figlet_format("vuln scan")
		print(ascii_banner)
		print("漏洞扫描工具(探测&利用)")
		print("1.XSS扫描(dalfox)\n2.46个POC扫描")
		num = input("请输入执行的扫描工具：")
		if num == '1':
			print("开始运行扫描工具")
			os.system('python3 dalfox.py')
			i=i+1
		if num == '2':
			print('开始运行扫描工具')
			os.system('python3 46poc.py')
			i=i+1
	if tool == '3':
		ascii_banner = pyfiglet.figlet_format("connect tool")
		print(ascii_banner)
		print("连接工具")
	if tool == '4':
		ascii_banner = pyfiglet.figlet_format("brute force")
		print(ascii_banner)
		print("暴力破解")
	if tool == '5':
		ascii_banner = pyfiglet.figlet_format("crypto tool")
		print(ascii_banner)
		print("密码工具")
	if tool == '6':
		ascii_banner = pyfiglet.figlet_format("social engineering")
		print(ascii_banner)
		print("社会工程学工具")
	if tool == '7':
		ascii_banner = pyfiglet.figlet_format("else tool")
		print(ascii_banner)
		print("其他工具")
