"""
    进程和线程的区别在于粒度不同, 进程之间的变量(或者说是内存)是不能直接互相访问的,
    而线程可以, 线程一定会依附在某一个进程上执行.我举个例子, 你在Windows下开一个IE浏览器,
    这个IE浏览器是一个进程. 你用浏览器去打开一个pdf, IE就去调用Acrobat去打开,
    这时Acrobat是一个独立的进程, 就是IE的子进程.而IE自己本身同时用同一个进程开了2个网页,
    并且同时在跑两个网页上的脚本, 这两个网页的执行就是IE自己通过两个线程实现的.值得注意的是,
    线程仍然是IE的内容, 而子进程Acrobat严格来说就不属于IE了, 是另外一个程序.之所以是IE的子进程,
    只是受IE调用而启动的而已.
"""

import multiprocessing
import threading
import os

def info(title):
    print(title)
    print("module name :",__name__)
    print("parent process is : ", os.getppid())
    print("process is : ", os.getpid())
    print("\n")

def run(name):
    while True:
        info('\033[31;1m function run \033[0m')
        print("hello ",name)

if __name__ == '__main__':
    info('\033[32;1mmain process line\033[0m')
    p1 = multiprocessing.Process(target=run, args=('hehe',))
    p2 = multiprocessing.Process(target=run, args=('test',))
    t1 = threading.Thread(target=run, args=('thread',))
    p1.start()
    p2.start()
    t1.start()
    p1.join()
    p2.join()
    t1.join()
    print(threading.active_count())
    print(threading.current_thread())
    run("bac")