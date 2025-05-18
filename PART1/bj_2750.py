import sys

arr = []
N = int(sys.stdin.readline())

for n in range(N):
    arr.append(int(input()))
    arr.sort()

for n in range(N):
    print(arr[n])
    
