#break 
for i in range(1,10):
    if i == 3:
        break
    print("output is:",i)

#continue 
for i in range (1,10):
    if i == 5:
        continue 
    print (i)

#pass
for i in range (1,5):
    if i == 2:
        pass
    print (i)

#for wtih else statement
for num in range(1,5):
    print(num)
    num += 1
else:
    print("Loop completed")

#while with else statement
num = 1
while num <= 5:
    print(num)
    num += 1
else:
    print("Loop completed")

