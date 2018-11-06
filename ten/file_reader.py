
# try:
#     with open('pi_digits.txt') as file_object:
#         contents = file_object.read()
#         print(contents)
# except IOError:
#     print("error")
# with open('C:\\Users\\ZaeMyn\\Desktop\\nfs.txt') as file_object:
# with open('C:/Users/ZaeMyn/Desktop/loopCreate.txt') as file_object:
filename = 'pi_digits.txt'
with open(filename) as file_object:
    contents = file_object.read()
    print(contents.rstrip())
print("--------------------\n")
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())
print("--------------------")
with open(filename) as file_object:
     lines = file_object.readlines()
     for line in lines:
        print(line.rstrip())