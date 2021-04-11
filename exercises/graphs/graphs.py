import random
import turtle
import math

turtle.tracer(False)
turtle.ht()


def random_maze_graph(n, m, per=60):
    A = []

    for j in range(m):
        for i in range(n):
            adj = []
            if i > 0:
                if (i + n * j) in A[i - 1 + n * j]:
                    adj += [i - 1 + n * j]
            if j > 0:
                if (i + n * j) in A[i + n * (j - 1)]:
                    adj += [i + n * (j - 1)]
            if i < (n - 1) and random.randrange(100) < per:
                adj += [(i + 1 + n * j)]
            if j < (m - 1) and random.randrange(100) < per:
                adj += [(i + n * (j + 1))]
            A += [adj]
    return A


def print_graph(A):
    for i in range(len(A)):
        print(str(i) + " -> " + str(A[i]))


def draw_maze_graph(A, n, m, s=20):
    turtle.tracer(False)
    turtle.pensize(4)
    turtle.pu()
    turtle.setposition(-n * s, -m * s)
    turtle.pd()
    turtle.setposition(n * s, -m * s)
    turtle.setposition(n * s, m * s)
    turtle.setposition(-n * s, m * s)
    turtle.setposition(-n * s, -m * s)
    for j in range(m):
        for i in range(n):
            if i > 0:
                if (i + n * j) not in A[i - 1 + n * j]:
                    turtle.pu()
                    turtle.setposition((2 * i - n) * s, (2 * j - m) * s)
                    turtle.pd()
                    turtle.setposition((2 * i - n) * s, (2 * j - m + 2) * s)
            if j > 0:
                if (i + n * j) not in A[i + n * (j - 1)]:
                    turtle.pu()
                    turtle.setposition((2 * i - n) * s, (2 * j - m) * s)
                    turtle.pd()
                    turtle.setposition((2 * i - n + 2) * s, (2 * j - m) * s)
    turtle.update()


def BFS(A, s):
    col = ["White"] * len(A)
    dis = [math.inf] * len(A)
    pre = [-1] * len(A)
    col[s] = "Gray"
    dis[s] = 0
    Q = [s]
    while len(Q) > 0:
        u = Q[0]
        Q = Q[1:]
        for v in A[u]:
            if col[v] == "White":
                col[v] = "Gray"
                dis[v] = dis[u] + 1
                pre[v] = u
                Q = Q + [v]
        col[u] = "Black"
    return (dis, pre)


# Demo I: BFS printed

##example = random_maze_graph(5, 5)
##print_graph(example)
##print(BFS(example, 12))

def draw_token(n, m, i, j, col, s=20):
    turtle.fillcolor(col)
    turtle.pu()
    turtle.setposition((2 * i - n + 0.5) * s, (2 * j - m + 1) * s)
    turtle.begin_fill()
    turtle.setposition((2 * i - n + 1) * s, (2 * j - m + 0.5) * s)
    turtle.setposition((2 * i - n + 1.5) * s, (2 * j - m + 1) * s)
    turtle.setposition((2 * i - n + 1) * s, (2 * j - m + 1.5) * s)
    turtle.setposition((2 * i - n + 0.5) * s, (2 * j - m + 1) * s)
    turtle.end_fill()


def BFS_maze_draw(A, s, n, m, z=20):
    turtle.tracer(True)
    turtle.speed(10)
    turtle.pensize(2)
    col = ["White"] * len(A)
    dis = [math.inf] * len(A)
    pre = [-1] * len(A)
    col[s] = "Gray"
    draw_token(n, m, (s % n), (s // n), "gray", z)
    dis[s] = 0
    Q = [s]
    while len(Q) > 0:
        u = Q[0]
        Q = Q[1:]
        ui = (u % n)
        uj = (u // n)
        for v in A[u]:
            if col[v] == "White":
                vi = (v % n)
                vj = (v // n)
                col[v] = "Gray"
                draw_token(n, m, vi, vj, "gray", z)
                dis[v] = dis[u] + 1
                pre[v] = u
                Q = Q + [v]
                turtle.pu()
                turtle.setposition((2 * ui - n + 1) * z, (2 * uj - m + 1) * z)
                turtle.pd()
                turtle.setposition((2 * vi - n + 1) * z, (2 * vj - m + 1) * z)
        col[u] = "Black"
        draw_token(n, m, ui, uj, "black", z)
    draw_token(n, m, (s % n), (s // n), "red", z)
    return (dis, pre)


# Demo 2: BFS drawn

##example = random_maze_graph(11, 9)
##
##draw_maze_graph(example, 11, 9, 32)
##turtle.update()
##
##BFS_maze_draw(example, 49, 11, 9, 32)
##turtle.update()


def DFS(A):
    col = ["White"] * len(A)
    pre = [-1] * len(A)
    dti = [-1] * len(A)
    fti = [-1] * len(A)
    time = 0
    for u in range(len(A)):
        if col[u] == "White":
            (col, pre, dti, fti, time) = DFS_Visit(A, u, col, pre, dti, fti, time)
    return pre


def DFS_Visit(A, u, col, pre, dti, fti, time):
    time = time + 1
    dti[u] = time
    col[u] = "Gray"
    for v in A[u]:
        if col[v] == "White":
            pre[v] = u
            (col, pre, dti, fti, time) = DFS_Visit(A, v, col, pre, dti, fti, time)
    col[u] = "Black"
    time = time + 1
    fti[u] = time
    return (col, pre, dti, fti, time)


def DFS_dm(A, n, m, z=20):
    turtle.tracer(True)
    turtle.speed(10)
    turtle.pensize(2)
    col = ["White"] * len(A)
    pre = [-1] * len(A)
    dti = [-1] * len(A)
    fti = [-1] * len(A)
    time = 0
    for u in range(len(A)):
        if col[u] == "White":
            (col, pre, dti, fti, time) = DFS_Visit_dm(A, n, m, u, col, pre, dti, fti, time, z)
            draw_token(n, m, (u % n), (u // n), "red", z)
    return pre


def DFS_Visit_dm(A, n, m, u, col, pre, dti, fti, time, z):
    time = time + 1
    dti[u] = time
    col[u] = "Gray"
    draw_token(n, m, (u % n), (u // n), "gray", z)
    for v in A[u]:
        if col[v] == "White":
            turtle.pu()
            turtle.setposition((2 * (u % n) - n + 1) * z, (2 * (u // n) - m + 1) * z)
            turtle.pd()
            turtle.setposition((2 * (v % n) - n + 1) * z, (2 * (v // n) - m + 1) * z)
            pre[v] = u
            (col, pre, dti, fti, time) = DFS_Visit_dm(A, n, m, v, col, pre, dti, fti, time, z)
    col[u] = "Black"
    draw_token(n, m, (u % n), (u // n), "black", z)
    time = time + 1
    fti[u] = time
    return (col, pre, dti, fti, time)


# draw_maze_graph(example, 5, 5)
# print(DFS(example))

# Demo 3: DFS drawn

example = random_maze_graph(11, 9, 50)

draw_maze_graph(example, 11, 9, 32)
turtle.update()

DFS_dm(example, 11, 9, 32)
turtle.update()