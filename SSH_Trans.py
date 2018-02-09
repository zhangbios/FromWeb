"""
    SSH 传输文件
"""

import paramiko


target_ip = 'localhost'
target_port = 22
target_user = 'test'
target_pswd = 'password'

# 创建传输对象
transport = paramiko.Transport((target_ip, target_port))
# 登录认证
transport.connect(username=target_user, password=target_pswd)
# 创建SFTP对象
sftp = paramiko.SFTPClient.from_transport(transport)
# 上传文件到 /opt 下， 存放名称改为 ssh_transe.txt
sftp.put('test', '/opt/ssh_transe.txt')
# 下载文件到当前目录下并改名为test2
sftp.get('/opt/ssh_transe.txt', 'test2')
transport.close()