"""
    多线程：
    ("当前线程数量：",threading.active_count())
    ("当前线程：",threading.current_thread())

"""
import threading, time


def run(n,m):
    print('running task',n,m)
    time.sleep(2)
    print('task down',n,m)


start_time = time.time()
t_objs = []
for i in range(50):
    str_value = str(i).encode('utf-8')
    # print("转换为字符：",str_value)
    # print("转换后的类型:",type(str_value))
    t = threading.Thread(target=run, args=('thread:',str_value))
    t.start()
    print("当前线程数量：",threading.active_count())
    print("当前线程：",threading.current_thread())
    t_objs.append(t)

for j in t_objs:
    t.join()

cost_time = time.time() - start_time
time.sleep(1)
print("all thread has finished...",threading.current_thread())
print('cost time:',cost_time)