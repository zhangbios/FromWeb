# 把方法变成静态属性--实例
class Flight(object):
    def __init__(self, name):
        self.name = name

    # 航空公司状态定义
    def check_status(self):
        print("checking flight %s status"%self.name)
        return 2

    @property
    def flight_status(self):
        status = self.check_status()
        if status == 0:
            print("flight canceled!!!")
        elif status == 1:
            print("flight already alive!!")
        elif status == 2:
            print("flight is comming!!")
        else:
            print("unrecognised status!")

    @flight_status.setter
    def flight_status(self, status):
        print("flight %s has changed status to %s"%(self.name, status))


def main():
    f = Flight("CZ6963")
    f.flight_status
    f.flight_status = 0


if __name__ == '__main__':
    main()