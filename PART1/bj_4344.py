C = int(input())
n = 0

for i in range(C):
    N_score = list(map(int, input().split()))
    avg = (sum(N_score) - N_score[0])/N_score[0]
    
    for i in range(N_score[0]):
        if N_score[i+1] > avg :
            n = n+1
    
    print(round(n/N_score[0]*100,3), "%")
    n = 0