def calculate_average(numbers):
    total = 0
    count = 0
    
    for num in numbers:
        total += num
        count += 1
    
    return total / count

# 测试用例
print(calculate_average([1, 2, 3, 4, 5]))  
print(calculate_average([])) 
print(calculate_average({"1","2","3","4","5"}))               
