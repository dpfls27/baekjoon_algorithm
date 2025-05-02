# 풀이1 세자리 자연수 끼리의 곱셈에서만 적용 가능

n = int(input())
n1,n2,n3 = map(int, input())

print(n*n3)
print(n*n2)
print(n*n1)

print(n*n1*100 + n*n2*10 + n*n3)

#풀이2 모든 곱셈에서 유효

a = int(input())
b = int(input())

b1 = a*(b%10)
b2 = a*((b%100-b%10)//10)
b3 = a*(b//100)

print(b1, b2, b3, b1+10*b2+100*b3)