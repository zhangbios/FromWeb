"""
面向对象编程 OOP
"""
# class
class Role(object):
    n = 1234
    n_list = []
    name = "变量类型"

    def __del__(self):
        print("%s 彻底死了！！" % self.name)

    def __init__(self, name, role, weapon, life_value=100, money=12000):
        # 类的属性
        self.name = name
        self.role = role
        self.weapon = weapon
        self.__life_value = life_value
        self.money = money

    def show_status(self):
        print("name:%s weapon:%s life_var:%s " % (self.name, self.weapon, self.__life_value))

    def __shot(self):  # 私有方法
        print("shoting.....")

    def get_shot(self):
        self.__life_value -= 50
        print("%s got shot!!" % self.name)

    def buy_gun(self, gun_name):
        print("%s bougt gun %s" % (self.name, gun_name))


# 继承
class People(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.friends = []

    def eat(self):
        print("%s is eating" % self.name)

    def sleep(self):
        print("%s is sleeping!!" % self.name)


class Relation(object):
    def __init__(self):
        print(self.name)

    def make_friends(self, obj):
        print("%s make friends with %s" % (self.name, obj.name))
        self.friends.append(obj)


class Man(People, Relation):
    # def __init__(self, name, age, money):
    #     super(Man,self).__init__(name,age)
    #     self.money = money
    #     print("%s has %s money"%(self.name,self.money))

    def drink(self):
        print("%s is drinking!" % self.name)

    def sleep(self):
        People.sleep(self)
        print("man is sleeping!")


class Woman(People, Relation):
    def get_birth(self):
        print("%s is bon a baby" % self.name)


# 多态
class Animal(object):
    def __init__(self, name):
        self.name = name

    def talk(self):
        pass

    @staticmethod
    def animal__talk(obj):
        obj.talk()


class Dog(Animal):
    def talk(self):
        print("wang wang!!")


class Cat(Animal):
    def talk(self):
        print("miao miao!!")


def main():
    # r1 = Role('zhangboss','police','ak99')
    # r2 = Role("lijie","jiji",'kb132')
    # # print(r1.__life._value)     # 私有属性不能被打印
    #
    # r1.show_status()        # 用这种方法调用私有属性
    # r1.get_shot()
    # r1.show_status()
    #
    # # r1.name = '李连杰'         # 修改类变量
    # # r1.bullet_prove = True     # 添加类变量
    # # r1.n = "change_value"
    # # r1.n_list.append(123)
    # # r2.n_list.append(2)
    # # del r1.weapon
    # # # r1.buy_gun('ssdsd')
    # #
    # # print(r1.n, r2.n)
    # # print(Role.n_list, r1.n_list, r2.n_list)
    # # print(r1.n, r1.name, r1.n_list, r1.bullet_prove)

    # r1 = Role("zhangboss", 'police', 'ak99')
    # r2 = Role("lijie", 'jiji', 'kb132')
    # r1.buy_gun("gege")
    # del r1
    # r2.get_shot()

    # # 继承
    #     m1 = Man("hahahah", 23)
    #     m1.eat()
    #     m1.drink()
    #     m1.sleep()
    #     w1 = Woman("bububu", 24)
    #     w1.get_birth()
    #     p1 = People("nimeia", 33)
    #     m1 = Man("hehe", 12, 100)
    #     m1.drink()
    #     m1.eat()
    #     m1.sleep()

    # # 多态
    #     d1 = Dog('hahaha')
    #     c1 = Cat('loo')
    #     # d1.talk()
    #     # c1.talk()
    #     Animal.animal__talk(d1)     # 多态语法：实现了对Animal接口的重用
    #     Animal.animal__talk(c1)

    # 多继承
    m1 = Man("zhangboss", 24)
    w1 = Woman("hehe", 22)
    w1.name = "呵呵哒"
    m1.make_friends(w1)
    print(m1.friends[0].name)


if __name__ == "__main__":
    main()
