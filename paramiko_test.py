"""
    实现SSH执行命令
"""

import paramiko


target_ip = 'localhost'
target_port = 22
target_user = 'test'
target_pswd = 'test123'

# 创建SSH对象
ssh = paramiko.SSHClient()
# 允许连接不在know_hosts文件中的主机
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# 开始连接服务器
ssh.connect(hostname=target_ip, port=target_port, username=target_user, password=target_pswd)
# 执行命令
stdin,stdout,stderr = ssh.exec_command('df')
# 收集命令执行结果
resault = stdout.read()
print(resault.decode())

# 三元运算实现
res,err = stdout.read(),stderr.read()
resault = res if res else err
print(resault.decode())
ssh.close()