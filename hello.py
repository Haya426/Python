#list methods
numbers = [1,4,5,7,8,3,2]
numbers.append(6) #append
numbers.insert(0,10) #insert
numbers.remove(10) #remove
# numbers.clear() #clear all
numbers.pop() #remove last item
numbers.sort() #sort ascending order
numbers.reverse() #sort descending order

print(numbers.index(2)) #return index 
print(50 in numbers) # return boolean value

numbers2 = numbers.copy() #copy list to another list
numbers.append(10)
print(numbers)
print(numbers2)