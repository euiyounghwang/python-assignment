# python-assignment
python-assignment (Deadline: Wednesday, November 15)


### Assignment
- Please use a well-known programming language such as Perl, C++, Java, Python, or PHP to develop code that takes two input files. --> __<i>Choose python environment with REST_API and Script for lookup the different keys from the source or files</i>__
-  Both input files consist of lines sorted in lexicographically ascending order based on ASCII values. The code should produce two output files:
- The first output file should contain lines that are present in the first input file but not in the second input file.
- The second output file should contain lines that are present in the second input file but not in the first input file.
- Solution: __<i>I have two ways to find different things in different files or strings using SWAGGER and Script</i>__

### Install Poerty
```
https://python-poetry.org/docs/?ref=dylancastillo.co#installing-with-the-official-installer
```

### Using Python Virtual Environment
```bash
python -m venv .venv
source .venv/bin/activate
```

### Using Poetry
- Create the virtual environment in the same directory as the project and install the dependencies with pytest:
```bash
poetry config virtualenvs.in-project true
poetry init
poetry add fastapi
poetry add uvicorn
poetry add pytz
poetry add pytest
poetry add pytest-cov
poetry add python-dotenv
poetry add httpx
poetry add asyncio
```

### Dataset
- Use dataset from 'https://raw.githubusercontent.com/dwyl/english-words/master/words.txt'

### Pytest
```bash
.venv) (base) ➜  php-restapi git:(master) ✗ pytest -v tests 
==================================================== test session starts ====================================================
platform darwin -- Python 3.9.7, pytest-7.4.3, pluggy-1.3.0 -- /Users/euiyoung.hwang/ES/Python_Workspace/python-assignment/.venv/bin/python
cachedir: .pytest_cache
rootdir: /Users/euiyoung.hwang/ES/Python_Workspace/python-assignment/tests
configfile: pytest.ini
plugins: cov-4.1.0, anyio-3.7.1
collected 5 items                                                                                                           

tests/test_api.py::test_mock_api PASSED                                                                               [ 20%]
tests/test_api.py::test_mock_lookup_api PASSED                                                                        [ 40%]
tests/test_lookup.py::test_skip SKIPPED (no way of currently testing this)                                            [ 60%]
tests/test_lookup.py::test_sample_string_sort PASSED                                                                  [ 80%]
tests/test_lookup.py::test_read_file_sort PASSED                                                                      [100%]
```