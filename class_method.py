class Dog(object):
    name = 123

    def __init__(self, name):
        self.name = name

    # def eat(self,food):
    #     print("%s is eating %s"%(self.name, food))
    #
    # 静态方法访问不了类或者实例中的任何属性
    # @staticmethod
    # def eat(self):
    #     print("%s is eating %s"%(self.name, "test"))

    # 类方法只能访问类变量，不能访问实例变量
    @classmethod
    def eat(self):
        print("%s is eating %s"%(self.name, 'sss'))

    def talk(self):
        print("%s is talking..."%self.name)


def main():
    d = Dog("hehe")
    # d.eat(d)
    d.eat()


if __name__ == "__main__":
    main()