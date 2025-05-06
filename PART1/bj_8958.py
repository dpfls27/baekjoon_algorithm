n = int(input()) 

number = []
a1 = 1

for i in range(n):
    Test = list(input()) 
    
    number.clear()
    a1 = 1
    
    for i in range(len(Test)):
        if Test[i] == 'O':
            number.append(a1)
            a1 = a1 + 1
            
        elif Test[i] =='X':
            number.append(0)  
            a1 = 1

    
    print(sum(number))    
