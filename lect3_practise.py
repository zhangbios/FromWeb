class School(object):
    def __init__(self, school, addr):
        self.school = school
        self.addr = addr
        self.students = []
        self.teachers = []
        self.stuffs = []

    def enrool(self, stu_obj):
        print("请为学员%s办理注册."%stu_obj.name)
        self.students.append(stu_obj)

    def hire(self, stuffs_obj):
        print("请为员工%s办理入职."%stuffs_obj.name)
        self.stuffs.append(stuffs_obj)


class SchoolMember(object):
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def tell(self):
        pass


class Teacher(SchoolMember):
    def __init__(self, name, age, sex, salary, course):
        super(Teacher,self).__init__(name, age, sex)
        self.salary = salary
        self.course = course

    def tell(self):
        print('''----info of teacher %s----
        Name:%s
        Age:%s
        Sex:%s
        Salary:%s
        Course:%s
        '''%(self.name,self.name, self.age, self.sex, self.salary, self.course))

    def teach(self):
        print("%s teach %s"%(self.name,self.course))


class Students(SchoolMember):
    def __init__(self, name, age, sex, stu_id, grade):
        super(Students,self).__init__(name, age, sex)
        self.stu_id = stu_id
        self.grade = grade

    def tell(self):
        print('''---info of student %s---
        Name:%s
        Age:%s
        Sex:%s
        Stu_id:%s
        Grade:%s'''%(self.name, self.name, self.age, self.sex, self.stu_id, self.grade))

    def pay_tuition(self,amount):
        print("请学员%s交学费%s"%(self.name, amount))


def main():
    school = School("清华大学","五道口")
    t1 = Teacher("张甫",30,"M",90000,"Techology")
    t2 = Teacher("康康",28,"F",150000,"Finance")
    s1 = Students("吴",8,"F",11030,"grade:1")
    s2 = Students("于",21,"M",11031,"grade:2")

    t1.tell()
    s1.tell()

    school.enrool(s1)
    school.enrool(s2)
    school.hire(t1)
    school.hire(t2)

    school.stuffs[0].teach()
    for stu in school.students:
        stu.pay_tuition(1000)

if __name__ == "__main__":
    main()