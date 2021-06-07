from reverse_words import reverse_words


def test_given():
    assert "Tadimeti V is name My" == reverse_words("My name is V Tadimeti")


def test_extra():
    assert "James is name my Hello" == reverse_words("Hello my name is James")
