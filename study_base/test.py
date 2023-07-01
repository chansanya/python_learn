import unittest


class User:

    def __init__(self, name, sex, age):
        self.name = name
        self.sex = sex
        self.age = age

    def info(self):
        print(f"这个人的名字叫：{self.name} 性别：{self.sex}，今年： {self.age}岁")


def add_attr(user_obj, attr_name, attr_val):
    setattr(user_obj, attr_name, attr_val)
    print(user_obj.__dict__)


class UserTest(unittest.TestCase):

    def test_user_info(self):
        user = User('大乔', '仙', 18)
        add_attr(user, 'skill', '流离')
        self. assertLessEqual(len(user.name), 10)
        self.assertGreaterEqual(user.age, 1)
        self.assertGreater(user.age, 0)
        self.assertRegex(user.sex, '^男%|^女%')


if __name__ == '__main__':
    print("开始执行单元测试")
    unittest.main()
