# 把方法变成静态属性
class Dog(object):
    def __init__(self, name):
        self.name = name
        self.__food = None

    # 实例化私有属性
    @property
    def eat(self):
        print("%s is eating %s"%(self.name, self.__food))

    @eat.setter
    def eat(self,food):
        self.__food = food
        print("set to food",food)

    @eat.deleter
    def eat(self):
        del self.__food
        print("删完了私有属性food")

    def talk(self):
        print("%s is talking..."%self.name)


def main():
    d = Dog("hihi")
    # d.eat()     # 不能被调用
    d.eat
    d.eat = "haha"
    # del d.name
    # print(d.name)
    d.eat
    del d.eat


if __name__ == '__main__':
    main()