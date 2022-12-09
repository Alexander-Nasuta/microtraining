def test_conversation_starter():
    import micropackage.big_brain_code as big_brain_bob
    alices_response = big_brain_bob.print_hi("Alice")
    assert alices_response is None


def test_love():
    import this
    import this as love

    statement = this is love
    assert statement is True

    statement = love is True
    assert statement is False
    statement = love is False
    assert statement is False

    statement = love is not False or True
    assert statement is True
    statement = love is love
    assert statement is True
