course1 = 'Python course for "beginner"'
course2 = "Python course for 'intermediate"
print(course1,course2)

#multiple lines strings
course = '''
Hi Jhon,
Welcome to our Python course,
Here is our email address,
Thank you for your support
'''
print(course)

#indexing strings
index = 'Python course for beginner'
print(index[1:-1]) #removing first and last character 
print(index[0]) #fisrt character 
print(index[-1]) #last character
print(index[0:3]) #return Pyt 
print(index[1:]) # return ython for beginner
print(index[:5]) # return Pytho

#copy strings
another = index[:]
print(another)

