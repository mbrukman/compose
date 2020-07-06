from pytest import raises

from composeml.data_slice.offset import DataSliceOffset


def test_numeric_typecast():
    assert int(DataSliceOffset('1 nanosecond')) == 1
    assert float(DataSliceOffset('1970-01-01')) == 0.0


def test_numeric_typecast_errors():
    match = 'offset must be position or period based'
    with raises(TypeError, match=match):
        int(DataSliceOffset('1970-01-01'))

    match = 'offset must be a timestamp'
    with raises(TypeError, match=match):
        float(DataSliceOffset('1 nanosecond'))


def test_invalid_value():
    with raises(AssertionError, match='invalid offset'):
        DataSliceOffset(None)


def test_alias_phrase():
    phrase = 'until start of next month'
    actual = DataSliceOffset(phrase).value
    expected = DataSliceOffset('1MS').value
    assert actual == expected