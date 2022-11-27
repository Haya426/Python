numbers = [2,2,3,4,5,6,6,7]
result = []
for i in numbers:
    if i not in result:
        result.append(i)
print(result)