#We are here gonna check the condition first and run the loop untill the condition becomes true

condition = 5

while(condition <50):
    print(condition)
    condition +=5

'''
The below flow basically allows the loop to run infinite times as the True is a boolean 
Once you run the loop break it and proceed further 
'''

'''
while True :
    print('Ha ha, fun')
'''



num = int(input("Enter the value, n ="))
if num<=0:
    print('Enter the absolute values')
else:
    sum=0
    while num>0:
        sum+=num
        num-=1

        print(sum)
        print(num)
