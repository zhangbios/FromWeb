import os
import sys
import copy


# print(os.path)
# cmd = os.system("dir")
# print(cmd)

print(sys.path)
print(sys.argv)
# print(sys.argv[1])
# 浅拷贝
a = ["hahahaha","xixixixi","lalalalalal",["hehe",123],"wuwuwu"]
b = copy.copy(a)
print(a)
print(b)
a[3][1] = 789
print(a)
print(b)

# 深拷贝
names = ["wanghui","huangjie","chenyibo","王辉",["alex","jack"]]
names2 = copy.deepcopy(names)
print(names)
print(names2)
names[-1][0]="ALEX"
print(names)
print(names2)