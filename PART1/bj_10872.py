import sys

N = int(sys.stdin.readline())
answer = 1

if N > 0:
    for i in range(1,N+1):
        answer *= i 

print(answer)   

# math 라이브러리 사용
# import math

# n = int(sys.stdin.readline())
# print(math.factorial(n))