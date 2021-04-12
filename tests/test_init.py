from lcm import cal_lcm

def test_false():
    assert cal_lcm(10, 20) == 1

def test_true():
    assert cal_lcm(10, 15) == 30
