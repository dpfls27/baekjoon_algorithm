# 내가 생각한 코드 
N , X = map(int, input().split()) # 단, 1 ≤ N, X ≤ 10,000
A = list(map(int, input().split()))
B =[]


for i in range(len(A)):
    
    if A[i] < X :
        B.append(A[i])

print(*B)

#  구글링 후 코드 

N, X = map(int, input().split())
A = list(map(int, input().split()))
for i in range(N):
    if A[i] < X:
        print(A[i], end = ' ')