"""
    多进程
"""
import multiprocessing,time,os

def run(name):
    print("{} is test".format(name))
    time.sleep(1)
    Thread = multiprocessing.cpu_count()
    print(Thread)
    print(os.getppid())     # 获取

if __name__ == '__main__':
    for i in range(10):
        m = multiprocessing.Process(target=run, args=("test:{}".format(i),))
        m.start()
        m.join()