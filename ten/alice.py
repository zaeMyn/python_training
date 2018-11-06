filename = 'alice.txt'
try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    print("文件不存在")
except ValueError:
    # print("")
    pass
else:
    print("文件存在")
    # 计算文件大致包含多少个单词
    words = contents.split()
    num_words = len(words)
    print("The file " + filename + " has about " + str(num_words) + " words.")