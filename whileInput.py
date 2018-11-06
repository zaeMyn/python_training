loopOrNot = True
message = input("请输入你的年龄(输入quit停止程序)：")
while loopOrNot and message != 'quit':
    try:
        print("你输入的是：" + str(int(message)))
        loopOrNot = False
    except ValueError:
        print("你输入的不是整数\n")
        message = input("请输入你的年龄(输入quit停止程序)：")


