myDimensions = (250,100)

print(myDimensions[0])
print(myDimensions[1])

#myDimensions[0] = 250
#you cant replace the original elements of the tuple.

myDimensions1 = (250,100)
print("Original Dimensions: ")
for dimension in myDimensions1:
    print(dimension)


myDimensions1 = (300,200)
print("Modified Dimensions: ")
for dimension in myDimensions1:
    print(dimension)

#you can redefine the same variable with different elements in tuple. 