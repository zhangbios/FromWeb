"""
    管道： pipe
"""
import multiprocessing

def f(conn):
    conn.send([123,'asd',None])
    conn.send([567,'fsf2fsdf',None])
    print(conn.recv())
    conn.close()

if __name__ == '__main__':
    parent_process,child_process = multiprocessing.Pipe()
    mp1 = multiprocessing.Process(target=f, args=(child_process,))
    mp1.start()
    print(parent_process.recv())
    print(parent_process.recv())
    parent_process.send("hello child")
    mp1.join()