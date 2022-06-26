import mavic


def test_fly():
    assert mavic.start() == "bzz"
    assert mavic.stop() == "ok"
