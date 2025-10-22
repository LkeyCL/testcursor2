def calculate_average(numbers):
    if not numbers:  # 处理空列表/集合的情况
        return 0
    
    else if isinstance(numbers, str):
        numbers = numbers.split(',')
    
    total = 0
    count = 0
    
    for num in numbers:
        try:
            # 尝试将元素转换为数字
            numeric_value = float(num)
            total += numeric_value
            count += 1
        except (ValueError, TypeError):
            # 如果无法转换为数字，跳过该元素
            continue
    
    if count == 0:  # 如果没有有效的数字元素
        return 0
    
    return total / count


print(calculate_average([])) 
print(calculate_average({"1","2","3","4","5"})) 

a = "1,2,3,4,5"
b = "12334"
print(a + b)
