alien_0 = {'color':'green','points':4}
print(alien_0['color'])
print(alien_0['points'])
# 转换字符类型
print(str(alien_0['points'])+"?")

alien_0['name'] = 'zzm'
alien_0['age'] = 18
print(alien_0)

# 创建空字典
alien_1 = {}
alien_1['name']='jxd'
alien_1['age'] = 17
print(alien_1)
# 删除键值对
del alien_1['age']
print(alien_1)