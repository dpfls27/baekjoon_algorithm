year = int(input()) #단, 1보다 크거나 같고 4000보다 작거나 같은 자연수

if (year % 4 == 0 and year%100 != 0) | (year%400 == 0 ) :
    print(1)
    
else:
    print(0)
