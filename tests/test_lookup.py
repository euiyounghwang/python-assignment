
import pytest
from inject.injector import util
import random

@pytest.mark.skip(reason="no way of currently testing this")
def test_skip():
    assert 1 != 1
    
    
def test_sample_string_sort():
    ''' test utils '''
    ''' pytest -sv tests/test_lookup.py::test_string_sort '''    
    test_inputs = ["car", "cAr", "apple", "banana", "fan", "dog"]
    results = util.sort_str_dict(test_inputs)
    assert results is not None
    assert results == {'apple': 1, 'banana': 2, 'cAr': 3, 'car': 4, 'dog': 5, 'fan': 6}
    

@pytest.mark.asyncio
async def test_read_file_sort():
    ''' pytest -sv tests/test_lookup.py::test_read_file_sort '''
    # --
    # test file before sorting
    inputs = await util.read_file('./dataset/a.txt')
    assert inputs is not None
    print(inputs)
    assert inputs ==  [
        "Abernant",
        "Abernathy",
        "Abernon",
        "abernethy",
        "aberr",
        "aberrance",
        "aberrancies",
        "aberrancy",
        "aberrant",
        "aberrantly"
    ]
    
    # --
    # test file after sorting
    # Shuffle list for testing 'sort_str_list' function
    # random.shuffle(inputs)
    
    inputs = util.sort_str_dict(inputs)
    assert inputs is not None
    print(inputs)
    assert inputs == {
        "Abernant":1,
        "Abernathy":2,
        "Abernon":3,
        "abernethy":4,
        "aberr":5,
        "aberrance":6,
        "aberrancies":7,
        "aberrancy":8,
        "aberrant":9,
        "aberrantly":10
    }
