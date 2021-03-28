def generate_empty_triangle_lists(n: int, init_value):
    arr = []
    for i in range(1, n+1):
        inner_arr = []
        for j in range(i):
            inner_arr.append(init_value)
        arr.append(inner_arr)
    return arr


def print_arr(arr: list[list]):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            print(arr[i][j], end=" ")
        print("")


def triangle_path_finish(a: list[list], b: list[list]):
    n = len(a)
    s = []
    j = 0

    for i in range(n-1):
        s.append(b[i][j])
        if b[i][j] == "right":
            j += 1
    return s


def triangle_path_dynamic(a: list[list]):
    n = len(a)
    b = generate_empty_triangle_lists(n-1, "#")
    c = generate_empty_triangle_lists(n, 0)

    for j in range(n):
        c[n-1][j] = a[n-1][j]
    for i in range(n-2, -1, -1):
        for j in range(i+1):
            if c[i+1][j] > c[i+1][j+1]:
                b[i][j] = "left"
                c[i][j] = c[i+1][j] + a[i][j]
            else:
                b[i][j] = "right"
                c[i][j] = c[i+1][j+1] + a[i][j]
    return triangle_path_finish(a, b)


A = [[3], [5, 8], [9, 2, 6], [4, 7, 3, 1]]

path = triangle_path_dynamic(A)
print(path)

