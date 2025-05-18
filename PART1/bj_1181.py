import sys

word = []
N = int(sys.stdin.readline())

for i in range(N):
    a = input()
    if a not in word: #중복 제거 있으면 넣지말고 없으면 넣어라 
        word.append(a)

word.sort()  # 먼저 사전 순 정렬
word.sort(key = lambda x : len(x))  # 그 다음 길이 순 정렬 list.sort(key=기준이 되는 함수)로 씀 

'''
    lambda함수란 무엇인가?
    lambda x: len(x)의 의미는 입력값 x를 받아 len(x)길이를 반환하는 함수 라는 의미 
    즉, key = len 인 셈이다 
    예를 들어, word = ['apple', 'a', 'cat', 'banana']라고 하자. 
    먼저, 사전순 정렬로 word = ['a', 'apple', 'banana', 'cat'] 이 된다 
    그 다음, lambda x : len(x)에 의해 a -> 1, apple-> 5, cat -> 3, banana -> 6 이됨 
    길이순 정렬로 [a, cat, apple, banana]
'''

for i in range(len(word)):
    print(word[i])
           
