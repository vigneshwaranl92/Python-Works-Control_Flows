'''for number in range(99,0,-1):
    if number > 1:
        print(number,"Bottles of beer on the wall",number,"bottles of beer")
        if number>2:
            suffix = str(number) + ",bottles of beer on the wall"
        else:
            suffix = '1 bottle of beer on the wall'
    elif number ==1:
        print('1 bottle of beer on the wall, 1 bottle of beer')
        suffix = ',No more beer on the wall'

    print('Take one down and pass it around', suffix)
    print('---')

   '''

for number in range(99,0,-1):
    if number > 1:
        print (number, "Bottles of beer on the wall" , number, "bolltes of beer")
        if number >2:
            suffix = str(number) + "bottles of beer on the wall"
        else:
            suffix = '1 bottle of beer on the wall'
    elif number ==1:
        print ('1 Bottle of beer on the wall, 1 bottle of beer')
        suffix = 'No more beer on the wall'
    print('Take one down and pass it around,' + suffix)
    print('---')

