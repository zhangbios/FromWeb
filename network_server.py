"""
socket:
    server: s.bind(address)
            s.listen(backlog)
            s.accept()      接受TCP连接并返回（conn,address）,其中conn是新的套接字对象，
                            可以用来接收和发送数据。address是连接客户端的地址。
    client: c.connect(address)
            c.connect_ex(address)
    public: p.recv(bufsize[,flag])
            p.send(string[,flag])
            p.sendall(string[,flag])
            p.recvfrom(bufsize[.flag])
            p.sendto(string[,flag],address)
            p.close()
            p.getpeername()
            p.getsockname()
            p.setsockopt(level,optname,value)
            p.getsockopt(levle,optname[,buflen])
            p.settimeou(timeout)
            p.gettimeout()
            p.fileno()
            p.setblocking(flag)
            p.makefile()
"""
import socket,os
server = socket.socket()
server.bind(('localhost',9985))
server.listen()

while True:
    conn,addr = server.accept()     # 监听
    print("开始连接",addr)
    while True:
        print("---等待新指令---")
        data = conn.recv(1024)
        if not data:
            break
        print("开始执行客户端命令",data)
        cmd_res = os.popen(data.decode()).read()
        print("接受之前：",len(cmd_res))
        if len(cmd_res) == 0:
            cmd_res = "cmd has no output ..."
        conn.send(cmd_res.encode('utf-8'))
        print("发送完成!")
server.close()