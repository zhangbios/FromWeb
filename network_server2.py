import socket
import os


IP = 'localhost'
port = 9999
# 服务器启用套接字绑定本地地址和端口
server = socket.socket()
server.bind((IP,port))
server.listen()

while True:
    conn,addr = server.accept()
    print("连接地址：",addr)
    while True:
        print("---------------------")
        print("等待新指令:")
        data = conn.recv(1024)
        if not data:
            print("连接已断开!")
            break
        elif data == b'q':
            print("接收到的命令：",data)
            print("断开连接!")
            conn.close()
            break
        else:
            print("执行命令",data)
            cmd_res = os.popen(data.decode()).read()
            print("回复命令的长度：",len(cmd_res))
            if len(cmd_res) == 0:
                cmd_res = "cmd has no output ..."
            # 先发送文件长度
            conn.send(str(len(cmd_res.encode())).encode('utf-8'))
            # 发送文件数据
            conn.send(cmd_res.encode('utf-8'))
            print("发送完成!")
