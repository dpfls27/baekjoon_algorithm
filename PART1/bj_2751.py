import sys

arr = []
N = int(sys.stdin.readline())

for n in range(N):
    arr.append(int(sys.stdin.readline()))

arr.sort()

for n in range(N):
    print(arr[n])
    
