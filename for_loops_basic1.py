for i in range(0, 151):                     #1
    print(i)



for i in range(5, 1001, 5):                 #2
    print(i)



for i in range(0, 101):
    if i % 10 == 0:
        print("Coding Dojo")                 #3
    elif i % 5 == 0:
        print("Coding")
    else:
        print(i)



sum = 0
for i in range(1, 500_001, 2):              #4
    sum += i
print(sum)



for i in range(2018, 0, -4):                #5
    print(i)




low_num = 2
high_num = 12
mult = 4                                    #6

for i in range(low_num, high_num + 1):
    if i % mult == 0:
        print(i)
