def play(obstacles: list[tuple[int, str]]) -> tuple[int, int]:
    v0 = 25
    m = 3
    h = 1
    g = 9.81
    theta = 45
    r = int(100 * v0**2 / g)

    return r, theta
