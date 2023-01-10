def selectGame(player):
    "选择游戏"
    print("\n")
    print("1:艾尔登法环")
    print("2:只狼")
    print("3:永劫无间")
    print("4:英雄联盟")
    return input(f"{player}!请选择你的游戏,按q退出:")

def play(gameCode):
    if   '1' == gameCode:
        print("==>:敬请见证")
        return True
    elif '2' == gameCode:
        print("==>:犹豫就会败北")
        return True
    elif '3' == gameCode:
        print("==>:垃圾游戏狗都不玩")   
        return True
    elif '4' == gameCode:
        print("==>:请打开WeGame交流")  
        return True
    elif 'q' == gameCode:
        print("==>:不玩了，再见。。。") 
        return False
    else:
        print("==>:请重新选择")  
        return True

def runPC():
    go = True;
    while(go):
        go = play(selectGame("阿褪"))


def setUser(name,age,**nila):
    nila["name"] = name;
    nila["age"] = age;
    return nila


def setAttr(name,*attr):
    print(f"姓名:{name} ,属性:{attr}")
    return attr


