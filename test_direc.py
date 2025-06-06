from snake.base import Direc


def test_opposite():
    assert Direc.opposite(Direc.UP) == Direc.DOWN
    assert Direc.opposite(Direc.DOWN) == Direc.UP
    assert Direc.opposite(Direc.LEFT) == Direc.RIGHT
    assert Direc.opposite(Direc.RIGHT) == Direc.LEFT
