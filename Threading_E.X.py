"""
    for example
"""
import threading,time


def run(n):
    print('task', n)
    time.sleep(5)


# 多线程并行：
t1 = threading.Thread(target=run, args=('t1',))
t1.start()
t2 = threading.Thread(target=run, args=('t2',))
t2.start()
# 单线程执行：
run(t1)
run(t2)