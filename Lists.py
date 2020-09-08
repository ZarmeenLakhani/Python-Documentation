x=1
print(str(x))
print(float(x))
bool(0) #only 0 is considered as false rest of the integers are considered true.even the negative ones
#sometimes a specific data type is required
fruit = 'banana'
len(fruit)
digits=[11,0,1,2,3,9,5,4,6,18]
digits.sort()
print(digits[-len(digits)])
print(digits[-1]) # last element
print(digits[0]) #first element
print(digits[-2]) # last element)
#Slicing
print(digits[:3])
print(digits[0:3])
#print(digit[:3]) all element startin from 0 till 2]]
#integer before 0 means
print(digits[3])
#pick 3rd item starting from 0
print(digits[0::7:2])
#okay so I will get all the elements of the list ( they're 7) which will be shown if they are multiple of 2
print(digits[::-1])
#basically reverses
#Note: make sure if the stride(multiple) is neg, than slicing is going toward left
#if the stride is positive, than slicing is going towards right
# basically you can't go
print(digits[0:5:-2]) #would return empty
print(digits[5:0:-2]) #instead you go from right to left.
for i in range(len(digits)):
    print(digits[0:i])
#Splitting and Joining
hobbies="reading, chess, coding, sudoku"
z= hobbies.split(", ")
print(z)
#turns string into a list
y= hobbies.split("chess")
print(y)
#['reading, ', ', coding, sudoku'] okay so before and after chess turned into elements of list.
joined=" and ".join(z)
print (joined)
csv=','.join(z)
print(csv)
