print("Hello Python world!")

# 变量
# 变量名只能包含字母、
# 数字和下划线。
# 变量名能以字母或下划线打头，但不能以数字打头。

msg= "你好啊"
print(msg)

msg= "我很好"
print(msg)

#字符串
#在Python中，用引号括起的都是字符串，其中的引号可以是单引号，也可以是双引号，如下所示：

test_str = "my name is leihuangyan";
print(test_str.title())
print(test_str.lower())
print(test_str.upper())
print(test_str.zfill(2))



## 练习
print("练习开始咯。。。。。。。。。。")
name  = "leihuangyan"

# 练习2-3：个性化消息
#  　用变量表示一个人的名字，并向其显示一条消息。显示的消息应非常简单，下面是一个例子。
format_str = f"{name} 敬请见证！！"
print(format_str)

# 练习2-4：调整名字的大小写
#  　用变量表示一个人的名字，再以小写、大写和首字母大写的方式显示这个人名。
print(name.lower())
print(name.upper())
print(name.title())


# 练习2-5：名言
#  　找一句你钦佩的名人说的名言，将其姓名和名言打印出来。输出应类似于下面这样（包括引号）。
# Albert Einstein once said, “A person who never made a mistake never tried anything new.”

print(f'{name} 说:"我已经会写了"')

#  练习2-7：剔除人名中的空白
#  　用变量表示一个人的名字，并在其开头和末尾都包含一些空白字符。务必至少使用字符组合"\t"
name  = "  leihuangyan  "
print(f"原来格式【{name}】")
print(f"去前空格【{name.lstrip()}】")
print(f"去后空格【{name.rstrip()}】")
print(f"去前后空格【{name.strip()}】")

# 练习2-8：数字8
#  　编写四个表达式，分别使用加法、减法、乘法和除法运算，但结果都是数字8。为使用函数调用print()
print(5+3) 
print(8-3)
print(2*4)
print(4<<1)
print("任意两个数相除时，结果总是浮点数，即便这两个数都是整数且能整除")
print(16/2)
print(16>>1)


# 练习2-9：最喜欢的数
# 用一个变量来表示你最喜欢的数，再使用这个变量创建一条消息，指出你最喜欢的数是什么，然后将这条消息打印出来。
like_number = 666
print ("你这波操作，我直呼 %d " % (like_number))
print (f"你这波操作，我直呼{like_number} ")


# 练习3-1：姓名
#  　将一些朋友的姓名存储在一个列表中，并将其命名为names#，依次访问该列表中的每个元素，从而将每个朋友的姓名打印出来。
names = ['辉少','骚球','茅坑']
for nameItem in names:
    print(f"{nameItem}，开黑了")
else:
    print("循环结束")
print(f"现在开黑有:{len(names)}")

# 添加到末尾
names.append("唐宇")
names.append("老鼠")
names.append("李鹏")
#插入到指定下标
names.insert(4,"老弟")
print(f"人来了，:{len(names)}人,分别是:{names}")

repeaceIndex = 4
replaceProple =names[repeaceIndex]
names[repeaceIndex] = "南瓜"
print(f"{replaceProple} 有事，叫了{names[repeaceIndex]}过来 现在有:{names}")

#出栈
runPeople = names.pop()
#下标推出
runPeople = names.pop(2)
#下标移除
del names[1]
#内容移除
names.remove("辉少")
print(f"诶 人跑了，现在只有:{len(names)}人了,还剩:{names}")



names3 = ['辉少','骚球','茅坑']
for nameItem2 in names:
    #循环下，无缩进的代码只会执行一次
    print(f"{nameItem2}，开黑了")
print("快快快上号")
    

print(f"现在开黑有:{len(names3)}")


#元组  不允许修改 ，只能重新赋值
group = ('艾希','奶妈')
for item in group:
    print(f"{item}，在下路")


group = ("锐雯","剑姬","刀妹")
for item in group:

    if  item == "锐雯":
        print(f"{item} 开启了折翼之舞")
    elif item == "剑姬":
        print(f"{item} 反手一秒四破")
    else:
        print("不认识");


# 字典

userInfo = {
    "name":"菈妮",
    "age":19,
    "job":"魔法师",
    "address":"交界地",
}

print(userInfo)
userInfo["lv"] = 400
print(userInfo)
userInfo["age"] = '?'
print(userInfo)
# 使用[]为空时报错
print(userInfo["name"])
# 使用get为空是返回None
print(userInfo.get("king"))

print("开始获取信息...")
for attr in userInfo:
    print(f"{attr}=>{userInfo.get(attr)}")


print()

# 引入模块
# 如果有指定别名，后续要用别名
import function as fun
print(fun.setUser("菈妮","未知",job="魔法师",address="魔法塔"))
print()

print(fun.setAttr("菈妮","半神","大魔法师","魔法塔"))
print()


# 指定模块的某个方法引入
from function import runPC as  start
start()

#全部引入 不推荐
# from function import  *
