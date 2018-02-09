import socket


IP = 'localhost'
port = 9999
client = socket.socket()
client.connect((IP,port))

while True:
    print("----------------------")
    cmd = input("请输入命令:").strip()
    if len(cmd) == 0:
        print("请输入正确的指令！")
        continue
    elif cmd == 'q':
        client.send(cmd.encode('utf-8'))
        print("程序退出!")
        client.close()
        break
    else:
        client.send(cmd.encode('utf-8'))
        cmd_res = client.recv(1024)
        print("接受到的数据：",cmd_res)
        received_size = 0
        received_data = b''
        while received_size < int(len(cmd_res.decode())):
            data = client.recv(1024)
            received_size += len(data)
            received_data += data
        print("cmd rees received done",received_size)
        print(received_data.decode())


