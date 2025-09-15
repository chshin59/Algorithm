import sys
sys.stdin = open("input.txt")

N = int(input())
A = list(map(int, input().split()))

answer = []
stack = []
while A:
    Ai = A.pop()

    NGE = -1
    while stack:
        if Ai < stack[-1]:
            NGE = stack[-1]
            break
        else:
            stack.pop()
    
    stack.append(Ai)
    answer.append(NGE)

print(*answer[::-1])
