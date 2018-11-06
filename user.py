# 遍历字典
user_0 = {
    'username': 'efermi',
    'last': 'fermi',
    'first': 'enrico'
}
# # 遍历键、值
# for key2,value2 in user_0.items():
#     print("\nkey:"+key2)
#     print("Value："+value2)
# for key in user_0.keys():
#     print("\nkey:"+key)
# for value in user_0.values():
#     print("\nvalue:"+value)
# # 按顺序遍历字典中的所有键
# for key in sorted(user_0.keys()):
#     print("\nKey:"+key)
# # 按顺序遍历字典中的所有值
# for value in sorted(user_0.values()):
#     print("\nvalue:"+value)
for value2 in sorted(user_0.values(),key=lambda s:s[2],reverse=True):#sorted(user_0,key,reverse(user_0)):
    print("\nvalue:"+value2+",Key3:")
for value2 in set(user_0.values()):
    print("\nvalue:"+value2)