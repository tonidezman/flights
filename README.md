# How to setup Dev Machine

```bash
# create virtual environment
$ python3 -m venv env

# Install dependencies
$ pip install -r requirements.txt
$ pip install -r requirements.test.txt

# copy .env.example, rename it to .env, and populate <...> with your local data
# script bellow creates and populates tables
$ python seed.py

# run local server
$ flask run
```

### Tests

```bash
$ python -m pytest ./tests
```

### Code Coverage

```bash
$ coverage run --omit 'env/*' -m pytest
$ coverage report
```
