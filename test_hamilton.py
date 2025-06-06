from snake.base import Direc, Map, PointType, Pos, Snake
from snake.solver import HamiltonSolver


def test_cycle():
    m = Map(6, 6)
    s = Snake(
        m, Direc.RIGHT, [Pos(1, 2), Pos(1, 1)], [PointType.HEAD_R, PointType.BODY_HOR]
    )
    solver = HamiltonSolver(s, False)
    table = solver.table
    cnt = 0
    ori_head = s.head()
    while True:
        head = s.head()
        assert cnt == table[head.x][head.y].idx
        s.move(solver.next_direc())
        cnt += 1
        if s.head() == ori_head:
            break
    assert cnt == m.capacity
