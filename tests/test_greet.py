from src.greet import greeting


def test_missing_user():
    assert greeting(None) == "Hello, friend!"
