from itertools import combinations
import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline

def tetromino(x, y, depth):
    if depth == 4:
        return board[x][y]

    visited[x][y] = 1
    cnt = board[x][y]

    if depth == 2:
        tmp = set()
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                tmp.add((nx, ny))
        if len(tmp) >= 2:
            for (x1, y1), (x2, y2) in combinations(tmp, 2):
                cnt = max(cnt, board[x][y] + board[x1][y1] + board[x2][y2])
    
    for d in range(4):
        nx, ny = x + dx[d], y + dy[d]
        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
            cnt = max(cnt, board[x][y] + tetromino(nx, ny, depth + 1))
    visited[x][y] = 0
    return cnt

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

answer = 0
for i in range(N):
    for j in range(M):
        answer = max(answer, tetromino(i, j, 1))

print(answer)
