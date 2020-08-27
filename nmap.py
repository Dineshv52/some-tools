import os

ip = input("请输入需要扫描的ip(可为ip段)：")
exp = 'nmap --reason -A '+ip+' -oN report.txt'
os.system(exp)
