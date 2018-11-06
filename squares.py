squares= []
print("计算1到10的平方")
for value in range(1,11):
    #square = value*value;
    square = value**2;
    squares.append(square);
    
    print(squares)
print("\n")
digits = range(0,9)
print(min(digits))
print(max(digits))
print(sum(digits))
'''列表解析 '''
squares3 = [value**2 for value in range(1,11)]
print(squares3)
'''
squares2= []
for value in range(1,11):
    squares2.append(value**2)
    print(squares2)
'''
    
