"""
    class Threading
"""
import threading,time


class MyThread(threading.Thread):
    def __init__(self, n):
        super (MyThread,self).__init__()
        self.n = n

    # 调用线程时，默认开启 run 方法
    def run(self):
        print('running task', self.n)
        time.sleep(5)

    # 无法随线程自动启用
    def test(self):
        print('this is a test',self.n)
        time.sleep(2)

t1 = MyThread('t1')
t2 = MyThread('t2')
t1.start()
t2.start()
