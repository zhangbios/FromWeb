import socket
import os
import hashlib


IP = 'localhost'
port = 9999
client = socket.socket()
client.connect((IP,port))

while True:
    cmd = input(">>:").strip()
    if len(cmd) == 0:
        continue
    # 检查字符串是否是以指定子字符串开头
    if cmd.startswith('get'):
        # 客户端发送指令
        return_value = client.send(cmd.encode())    # client send 1
        print("发送成功返回值：",return_value)
        # 客户端接收server端消息
        server_response = client.recv(1024)         # recv server 2     接收filename
        print("server response:",server_response)
        return_value2 = client.send("准备接收文件".encode())  # client send 3  准备接收文件
        print("判断是否发送成功：",return_value2)
        # 计算服务端返回文件的长度
        file_total_size = len(server_response.decode())
        print("服务器返回filename长度：",file_total_size)
        received_size = 0
        # 将客户端发送指令分解为 path + filename 格式
        filename = cmd.split()[1]
        f = open(filename + '.new', 'wb')
        m = hashlib.md5()

        while received_size < file_total_size:
            data = client.recv(1024)    # recv server 4     接收文件内容
            received_size += len(data)
            print("接收到的数据:",data)
            # 生成客户端接收的MD5
            m.update(data)
            # 写入数据
            f.write(data)
        else:
            new_file_md5 = m.hexdigest()
            print("文件接收完毕，文件名长度{}，文件大小{}".format(file_total_size,received_size))
            f.close()
        server_md5 = client.recv(1024)      # client recv 5    接收MD5 值
        print(server_md5, new_file_md5)
client.close()