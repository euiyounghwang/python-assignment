# python-assignment
python-assignment


### Assignment
- Please use a well-known programming language such as Perl, C++, Java, Python, or PHP to develop code that takes two input files. --> __<i>Choose python environment with REST_API and Script for lookup the different keys from the source or files</i>__
-  Both input files consist of lines sorted in lexicographically ascending order based on ASCII values. The code should produce two output files:
- The first output file should contain lines that are present in the first input file but not in the second input file.
- The second output file should contain lines that are present in the second input file but not in the first input file.

### Install Poerty
```
https://python-poetry.org/docs/?ref=dylancastillo.co#installing-with-the-official-installer
```

Using Python Virtual Environment
```bash
python -m venv .venv
source .venv/bin/activate
```

Using Poetry: Create the virtual environment in the same directory as the project and install the dependencies:
```bash
poetry config virtualenvs.in-project true
poetry init
poetry add fastapi
poetry add uvicorn
poetry add pytz
```

Pytest
```bash
.venv) (base) ➜  php-restapi git:(master) ✗ pytest -v tests 

```