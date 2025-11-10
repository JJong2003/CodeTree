def isBeautiful(number):
    leng = len(number)
    check = [False] * leng
    for i in range(leng):
        if check[i]: continue
        
        search_bound = i + int(number[i])
        if search_bound > len(number):
            return False
        
        for j in range(i, search_bound):
            check[j] = True
            if number[i] != number[j]:
                return False

    return True


def btk(number, limit, depth=0):
    if depth == limit:
        valid = isBeautiful(number)
        if valid:
            return 1
        return 0
    
    cnt = 0
    for i in range(1, 4+1):
        cnt += btk(number + str(i), limit, depth+1)
    return cnt

if __name__ == '__main__':
    n = int(input())
    answer = btk("", n)
    print(answer)