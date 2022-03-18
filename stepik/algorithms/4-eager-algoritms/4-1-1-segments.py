def cover_segments_by_points():
    n = int(input())

    arr = [[0 for x in range(2)] for y in range(n)]

    i = 0
    while (i < n):
        l, r = map(int, input().split())
        arr[i][0] = l
        arr[i][1] = r
        i = i + 1

    i = 0
    while (i < n):
        min = arr[i][1]
        j = i + 1
        while (j < n):
            if (arr[j][1] < min):
                lTemp = arr[j][0]
                rTemp = arr[j][1]
                arr[j][0] = arr[i][0]
                arr[j][1] = min
                arr[i][0] = lTemp
                arr[i][1] = rTemp
                min = rTemp
            j = j + 1
        i = i + 1

    np = 1
    tp = arr[0][1]

    l = [tp]

    i = 1
    while (i < n):
        if (arr[i][0] > tp):
            np = np + 1
            tp = arr[i][1]
            l.append(tp)
        i = i + 1

    print(np)

    for x in l:
        print(x, end=" ")


if __name__ == '__main__':
    cover_segments_by_points()
