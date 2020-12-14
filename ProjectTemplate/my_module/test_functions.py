"""Test for my functions.

Note: because these are 'empty' functions (return None), here we just test
  that the functions execute, and return None, as expected.
"""

from my_module.functions import introduction_maker, content_filler, conclusion_creator, nonsense_generator

def test_introduction_maker():
    assert isinstance(introduction_maker('cat'), str)
    assert 'cat' in introduction_maker('cat')
    try:
        introduction_maker(1)
    except ValueError:
        assert True

def test_content_filler():
    assert isinstance(content_filler('cat'), str)
    assert 'cat' in content_filler('cat')
    try:
        content_filler(1)
    except ValueError:
        assert True

def test_conclusion_creator():
    assert isinstance(conclusion_creator('cat'), str)
    assert 'cat' in conclusion_creator('cat')
    try:
        conclusion_creator(1)
    except ValueError:
        assert True

def test_nonsense_generator():
    try:
        nonsense_generator(1,100,2,'essay')
    except ValueError:
        assert True
    try:
        nonsense_generator('cat',100,0,'essay')
    except ZeroDivisionError:
        assert True
    try:
        nonsense_generator('cat',100,0,'i am fine')
    except TypeError:
        assert True
    