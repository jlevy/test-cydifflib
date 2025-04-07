import cydifflib


def test_cydifflib():
    s = cydifflib.SequenceMatcher(None, ["a", "b"], ["a", "c"], autojunk=False)
    print(s)
