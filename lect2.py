# import sys,os
#
# print(os.path.abspath(__file__))
# print(os.path.dirname(os.path.abspath(__file__)))
# print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# 导入技巧：
import sys,os
DASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODULE_DIR = os.path.dirname(DASE_DIR)
print(MODULE_DIR)
sys.path.append(MODULE_DIR)
# import module_name

# 标准库：
# time:
import time

t = time.time()
x = t
print(x)

q = time.localtime()
print(q)

w = time.timezone / 3600
print(w)

e = time.altzone
print(e / 3600)

time.sleep(10)

r = time.gmtime()
print(r)



