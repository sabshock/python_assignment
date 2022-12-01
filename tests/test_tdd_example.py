from src.tdd_example import TDDExample

tdd_example_instance = TDDExample()

def test_reverse_string():
    text = 'python'
    expected = 'nohtyp'

    actual = tdd_example_instance.reverse_string(text)

    assert expected == actual

def test_find_longest_word():
    sentence = '''
        Lorem ipsum dolor sit amet, consectetur adipiscing elit.
    '''
    expected = 'consectetur'
    actual = tdd_example_instance.find_longest_word(sentence)

    assert expected == actual

def test_reverse_list():
    expected = [10,2,5,22,77]
    actual = tdd_example_instance.reverse_list([77,22,5,2,10])

    assert expected == actual

def test_count_digits():
    expected = 3

    actual = tdd_example_instance.count_digits([7, 1, 7, 2, 7,10,77], 7)

    assert expected == actual
