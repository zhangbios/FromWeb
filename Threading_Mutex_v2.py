"""
    信号量 互斥锁
    Semaphore 是同时允许一定数量的线程更改数据
"""

import threading,time
num = 0
same = threading.BoundedSemaphore(5)
t_objs = []

def run(n):
    same.acquire()
    print("run threading :",n)
    time.sleep(5)
    global num
    num += 1
    same.release()

for i in range(40):
    t = threading.Thread(target=run,args=(i,))
    t.start()
    t_objs.append(t)

for obj in t_objs:
    obj.join()

while threading.active_count() != 1:
    print("threading active count:",threading.active_count())
else:
    print("all threading over...")
    print(num)
