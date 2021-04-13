from lcm import cal_lcm

def test_a():
    assert cal_lcm(10, 20) == 20

def test_b():
    assert cal_lcm(10, 15) == 30
