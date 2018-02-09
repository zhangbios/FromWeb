"""
    python thread event 用于主线程控制其他线程执行，事件主要提供了三个方法：
    set wait clear
    事件处理方法：
        全局定义了一个flag，
        当 flag 为false，当程序执行 event.wait 方法时就会阻塞
        当 flag 为True时，event.wait方法时就不会阻塞
"""
import threading
import time

# flag = False
event = threading.Event()

def tranffic_litght():
    count = 0
    event.set()
    while True:
        if count > 3 and count < 6:
            event.clear()
            print("traffic lighter change red!")
        elif count > 6:
            event.set()
            count = 0
        else:
            print("traffic lighter is green!")
        time.sleep(1)
        count += 1

def car(name):
    while True:
        if event.is_set():
            print("{} can across the road!".format(name))
            time.sleep(1)
        else:
            print("{} can not cross the road!".format(name))
            event.wait()
            print("traffic lighter change to green, {} can cross".format(name))

def main():
    t1 = threading.Thread(target=tranffic_litght)
    t2 = threading.Thread(target=car,args=("mini cooper",))
    t1.start()
    t2.start()

if __name__ == '__main__':
    main()