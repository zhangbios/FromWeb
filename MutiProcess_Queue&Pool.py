"""
    Queue 队列
    Pool  进程池
"""
from multiprocessing import Pool,Process,Queue
import time,os,random

def write(que):
    for char in ['a', 'b', 'c']:
        print('put {} to queue..'.format(char))
        que.put(char)
        time.sleep(3)

def read(que):
    while True:
        if not que.empty():
            value = que.get(True)
            print("get queue char :",value)
            time.sleep(random.random())
        else:
            break

def pool_test(n):
    print("task process : ",n)
    time.sleep(3)
    print("cpu count: ", os.cpu_count())

if __name__ == '__main__':
    que = Queue()
    proc1 = Process(target=write, args=(que,))
    proc2 = Process(target=read, args=(que,))
    proc1.start()
    proc1.join()
    proc2.start()
    proc2.join()
    # print("-------------------------------")
    # p = Pool()
    # for i in range(10):
    #     p.apply_async(pool_test, args=(i,))
    # print("wait for all subprocess done....")
    # p.close()
    # p.join()
    # print("all subprocess done.")
