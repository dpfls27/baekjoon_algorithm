N = int(input())
# 소수는 1과 자기자신만 약수로 가지는 수 

number = list(map(int, input().split()))
count = 0 

for n in number:
    for i in range(2, n+1):
        if n % i == 0:
            if n == i:
                count += 1 
            break

print(count)
        