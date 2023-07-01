import traceback
from random  import randint


while  True:
    num = int(input("请输入一个数:"))
    rnum = randint(0, 100)
    try:
        print(f"计算的结果为:{rnum / num}")
    except Exception:
        # print(f"输入值异常{num}")
        traceback.print_exc()
        pass
    else:
        print(f"正常值{num}")