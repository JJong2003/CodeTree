def bomb1(grid, y, x):
    for i in range(5):
        if (y-2 + i < 0) or (y-2 + i >= len(grid) or grid[y-2 +i][x] == 1): continue
        grid[y-2 + i][x] = -1

def repair_bomb1(grid, y, x):
    for i in range(5):
        if (y-2 + i < 0) or (y-2 + i >= len(grid)) or (grid[y-2 +i][x] == 1): continue
        grid[y-2 + i][x] = 0

def bomb2(grid, y, x):
    for i in range(3):
        idx_x = x-1+i
        if (idx_x < 0) or (idx_x >= len(grid)) or (grid[y][idx_x] == 1): continue
        grid[y][idx_x] = -1

        idx_y = y-1+i
        if (idx_y < 0) or (idx_y >= len(grid)) or (grid[idx_y][x] == 1): continue
        grid[idx_y][x] = -1

def repair_bomb2(grid, y, x):
    for i in range(3):
        idx_x = x-1+i
        if (idx_x < 0) or (idx_x >= len(grid)) or (grid[y][idx_x] == 1): continue
        grid[y][idx_x] = 0

        idx_y = y-1+i
        if (idx_y < 0) or (idx_y >= len(grid)) or (grid[idx_y][x] == 1): continue
        grid[idx_y][x] = 0

def bomb3(grid, y, x):
    for i in range(3):
        idx_x = x-1+i
        idx_y = y-1+i
        if (idx_x < 0) or (idx_x >= len(grid)) or (grid[y][idx_x] == 1): continue
        if (idx_y < 0) or (idx_y >= len(grid)) or (grid[idx_y][x] == 1): continue
        grid[idx_y][idx_x] = -1

    for i in range(3):
        idx_x = x-1+i
        idx_y = y+1+i
        if (idx_x < 0) or (idx_x >= len(grid)) or (grid[y][idx_x] == 1): continue
        if (idx_y < 0) or (idx_y >= len(grid)) or (grid[idx_y][x] == 1): continue
        grid[idx_y][idx_x] = -1

def repair_bomb3(grid, y, x):
    for i in range(3):
        idx_x = x-1+i
        idx_y = y-1+i
        if (idx_x < 0) or (idx_x >= len(grid)) or (grid[y][idx_x] == 1): continue
        if (idx_y < 0) or (idx_y >= len(grid)) or (grid[idx_y][x] == 1): continue
        grid[idx_y][idx_x] = 0

    for i in range(3):
        idx_x = x-1+i
        idx_y = y+1+i
        if (idx_x < 0) or (idx_x >= len(grid)) or (grid[y][idx_x] == 1): continue
        if (idx_y < 0) or (idx_y >= len(grid)) or (grid[idx_y][x] == 1): continue
        grid[idx_y][idx_x] = 0

def bomb(grid, limit, bomb_info, depth=0):
    if depth == limit:
        # 초토화 된 영역의 수
        cnt = 0
        for i in range(n):
            for j in range(n):
                if grid[i][j] in [-1, 1]:
                    cnt += 1
        
        # for elem in grid:
        #     print(elem)
        # print(depth)
        return cnt

    ans = 0
    for y, x in bomb_info[depth:]:
        bomb1(grid, y, x)
        ans = max(ans, bomb(grid, limit, bomb_info, depth+1))
        repair_bomb1(grid, y, x)
        
        bomb2(grid, y, x)
        ans = max(ans, bomb(grid, limit, bomb_info, depth+1))
        repair_bomb2(grid, y, x)

        bomb3(grid, y, x)
        ans = max(ans, bomb(grid, limit, bomb_info, depth+1))
        repair_bomb3(grid, y, x)
    return ans


n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
bomb_info = []
for i in range(n):
    for j in range(n):
        if grid[i][j] == 1:
            bomb_info.append((i, j))

ans = bomb(grid, len(bomb_info), bomb_info)
print(ans)