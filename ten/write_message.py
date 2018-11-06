# 写入多行，如果文件存在，会被清空，并写入新的内容
filename = 'programming.txt'
with open(filename, 'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I am zzm.\n")
# 附加内容，不删除
with open(filename, 'a') as file_object:
    file_object.write("我是附加的内容.\n")