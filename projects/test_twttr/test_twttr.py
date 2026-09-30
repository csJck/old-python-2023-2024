from twttr import shorten

def test_vowe():
    assert shorten("unquestionable") == "nqstnbl"

def test_nums():
    assert shorten("123unquestionable") == "123nqstnbl"

def test_punc():
    assert shorten("!?unquestionable") == "!?nqstnbl"

def test_caps():
    assert shorten("UNQUESTIONABLE") == "NQSTNBL"







