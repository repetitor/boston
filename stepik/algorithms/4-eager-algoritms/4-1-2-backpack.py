"""
Задача: непрерывный рюкзак
Выведите максимальную стоимость частей предметов
(от каждого предмета можно отделить любую часть, стоимость и объём при этом пропорционально уменьшатся),
помещающихся в данный рюкзак, с точностью не менее трёх знаков после запятой.
"""


def fill_backpack():
    n, capacity = map(int, input().split())  # input: <количество предметов> <вместимость рюкзака>

    cost_volume_items = [[0 for _ in range(2)] for _ in range(n)]
    i = 0
    while i < n:
        cost_item, volume_item = map(int, input().split())  # input: <cost> <volume>
        cost_volume_items[i][0] = cost_item
        cost_volume_items[i][1] = volume_item
        i = i + 1

    # price=cost/volume order by desc
    i = 0
    while i < n:
        j = i + 1
        while j < n:
            max_price = cost_volume_items[i][0] / cost_volume_items[i][1]
            if cost_volume_items[j][0] / cost_volume_items[j][1] > max_price:
                cost_volume_items[i][0], cost_volume_items[j][0] = cost_volume_items[j][0], cost_volume_items[i][0]
                cost_volume_items[i][1], cost_volume_items[j][1] = cost_volume_items[j][1], cost_volume_items[i][1]
            j = j + 1
        i = i + 1

    volume_result = 0
    cost_result = 0
    i = 0
    while volume_result < capacity and i < n:
        free_volume = capacity - volume_result
        if cost_volume_items[i][1] < free_volume:
            cost_result += cost_volume_items[i][0]
            volume_result += cost_volume_items[i][1]
        else:
            cost_result += free_volume * cost_volume_items[i][0] / cost_volume_items[i][1]
            volume_result = capacity
        i = i + 1

    print(f"{cost_result:.3f}")


def fill_backpack_v2():
    n, capacity = map(int, input().split())

    # cost_volume_items = [[map(int, input().split())] for _ in range(n)] - error
    cost_volume_items = [tuple(map(int, input().split())) for _ in range(n)]

    cost_volume_items.sort(key=lambda x: x[0] / x[1], reverse=True)

    cost_result = 0
    for item in cost_volume_items:
        if item[1] < capacity:
            cost_result += item[0]
            capacity -= item[1]
        else:
            cost_result += capacity * item[0] / item[1]
            break

    print(f"{cost_result:.3f}")


def v3():
    n, v = list(map(int, input().split()))
    items = [list(map(int, input().split())) for i in range(n)]

    items = sorted(items, key=lambda i: i[0] / i[1], reverse=True)
    C = 0
    while v and items:
        item = items.pop(0)
        packed = min(item[1], v)
        C += packed * item[0] / item[1]
        v -= packed

    print(C)


if __name__ == '__main__':
    # fill_backpack()
    fill_backpack_v2()
    # v3()
