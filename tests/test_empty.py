def test_empty():
    assert True


def test_main():
    from project import main

    assert main() is None
    assert main(0) == 0
