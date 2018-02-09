import paramiko

target_ip = 'localhost'
target_port = 22
target_user = 'test'
target_pswd = 'password'
filename = 'id_rsa'

private_key = paramiko.RSAKey.from_private_key_file(filename)
# 实例化SSH
ssh = paramiko.SSHClient()
# 自动添加到对方的know_host文件
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# 使用私钥连接机器
ssh.connect(hostname=target_ip, port=target_port, username=target_user, pkey=private_key)
stdin,stdout,stderr = ssh.exec_command('dir')
result_value = stdout.read()
print(result_value.decode())

res,err = stdout.read(),stderr.read()
result_value = res if res else err


