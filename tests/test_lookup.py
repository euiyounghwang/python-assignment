
import pytest
from injector import util
import random

@pytest.mark.skip(reason="no way of currently testing this")
def test_skip():
    assert 1 != 1
    
    
def test_mock_api(mock_client):
    response = mock_client.get("/v1")
    assert response is not None
    assert response.status_code == 200
    assert response.json() == {
        "message": "Hello World"
    }
    
    
def test_sample_string_sort():
    ''' test utils '''
    ''' pytest -sv tests/test_lookup.py::test_string_sort '''    
    test_inputs = ["car", "cAr", "apple", "banana", "fan", "dog"]
    results = util.sort_str_list(test_inputs)
    assert results is not None
    assert results == {'apple': 1, 'banana': 2, 'cAr': 3, 'car': 4, 'dog': 5, 'fan': 6}
    

def test_read_file_sort():
    ''' pytest -sv tests/test_lookup.py::test_read_file_sort '''
    # --
    # test file before sorting
    inputs = util.read_file('./dataset/a.txt')
    assert inputs is not None
    # print(inputs)
    assert inputs == [
        "Abey",
        "abeyance",
        "abeyances",
        "abeyancy",
        "abeyancies",
        "abeyant",
        "abeigh",
        "ABEL",
        "Abelard",
        "abele",
        "abeles",
        "Abelia",
        "Abelian",
        "Abelicea",
        "Abelite",
        "Abell",
        "Abelmoschus",
        "abelmosk",
        "abelmosks",
        "abelmusk",
        "Abelonian",
        "Abelson",
        "abeltree",
        "Abencerrages",
        "abend",
        "abends",
        "Abenezra",
        "abenteric",
        "Abeokuta",
        "abepithymia",
        "ABEPP",
        "Abercromby",
        "Abercrombie",
        "Aberdare",
        "aberdavine",
        "Aberdeen",
        "Aberdeenshire",
        "aberdevine",
        "Aberdonian",
        "aberduvine",
        "Aberfan",
        "Aberglaube",
        "Aberia",
        "Aberystwyth",
        "Abernant",
        "Abernathy",
        "abernethy",
        "Abernon",
        "aberr",
        "aberrance",
        "aberrancy",
        "aberrancies",
        "aberrant",
        "aberrantly"
    ]
    
    # --
    # test file after sorting
    # Shuffle list for testing 'sort_str_list' function
    random.shuffle(inputs)
    
    inputs = util.sort_str_list(inputs)
    assert inputs is not None
    # print(inputs)
    assert inputs == {
        "ABEL":1,
        "ABEPP":2,
        "Abelard":3,
        "Abelia":4,
        "Abelian":5,
        "Abelicea":6,
        "Abelite":7,
        "Abell":8,
        "Abelmoschus":9,
        "Abelonian":10,
        "Abelson":11,
        "Abencerrages":12,
        "Abenezra":13,
        "Abeokuta":14,
        "Abercrombie":15,
        "Abercromby":16,
        "Aberdare":17,
        "Aberdeen":18,
        "Aberdeenshire":19,
        "Aberdonian":20,
        "Aberfan":21,
        "Aberglaube":22,
        "Aberia":23,
        "Abernant":24,
        "Abernathy":25,
        "Abernon":26,
        "Aberystwyth":27,
        "Abey":28,
        "abeigh":29,
        "abele":30,
        "abeles":31,
        "abelmosk":32,
        "abelmosks":33,
        "abelmusk":34,
        "abeltree":35,
        "abend":36,
        "abends":37,
        "abenteric":38,
        "abepithymia":39,
        "aberdavine":40,
        "aberdevine":41,
        "aberduvine":42,
        "abernethy":43,
        "aberr":44,
        "aberrance":45,
        "aberrancies":46,
        "aberrancy":47,
        "aberrant":48,
        "aberrantly":49,
        "abeyance":50,
        "abeyances":51,
        "abeyancies":52,
        "abeyancy":53,
        "abeyant":54
    }
