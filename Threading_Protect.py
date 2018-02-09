"""
    threading.Thtead.setDaemon()
"""

import threading,time


def run(n,m):
    print('running task',n,m)
    time.sleep(2)
    print('task down',n,m)


start_time = time.time()
t_objs = []
for i in range(50):
    t = threading.Thread(target=run,args=('thread:',i))
    # 设置当前线程为守护线程
    t.setDaemon(True)
    t.start()
    print("当前线程数量：",threading.active_count())
    print("当前线程：",threading.current_thread())
    t_objs.append(t)

# for obj in t_objs:
#     obj.join()

cost_time = time.time() - start_time
print("cost time",cost_time)




