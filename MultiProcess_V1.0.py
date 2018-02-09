"""
    多进程 解决多核问题而生
"""

# 单进程
import multiprocessing,time

def run(name):
    time.sleep(1)
    print("hello {}!".format(name))

if __name__ == '__main__':
    m = multiprocessing.Process(target=run,args=("world",))
    m.start()
    # 等待进程
    m.join()

