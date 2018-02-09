"""
    线程锁 == 互斥锁
"""
import threading,time

num = 0
lock = threading.Lock()
t_obj = []

def run(n):
    lock.acquire()
    print("thread:",n)
    global num
    num += 1
    time.sleep(1)
    lock.release()

for i in range(50):
    values = str(i)
    t = threading.Thread(target=run, args=("thread:%s"%values,))
    print(t)
    t.start()
    t_obj.append(t)

for obj in t_obj:
    obj.join()

print(num)