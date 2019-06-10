# Tests

### Setup
Make sure you executed the steps described [here](./INSTALL.md).

### Unit Tests
```
source .env/bin/activate
nosetests \
    --cover-min-percentage 80 \
    --cover-erase \
    --cover-tests \
    --exclude=functional \
    --with-coverage \
    --cover-package "app" \
    tests
```
Expected Results:
```
............................................................
Name                                    Stmts   Miss  Cover   Missing
---------------------------------------------------------------------
app/__init__.py                             0      0   100%
app/api/__init__.py                        39      0   100%
app/api/auth.py                            39      0   100%
app/api/constants.py                       44      0   100%
app/api/controller/__init__.py              8      0   100%
app/api/controller/models/__init__.py       5      0   100%
app/api/controller/models/movie.py         33      0   100%
app/api/controller/models/person.py        57      0   100%
app/api/controller/models/role.py          25      0   100%
app/api/controller/models/user.py          48      0   100%
app/api/controller/models/utils.py         21      0   100%
app/api/controller/movies.py               70      0   100%
app/api/controller/people.py              120      0   100%
app/api/controller/roles.py                80     60    25%
app/api/controller/users.py                77      0   100%
app/api/errors.py                          76      0   100%
app/api/health.py                           7      0   100%
app/api/movies.py                          73     16    78%
app/api/people.py                          83     20    76%
app/api/roles.py                          100     48    52%
app/api/serializers.py                     57     38    33%
---------------------------------------------------------------------
TOTAL                                    1062    182    83%
----------------------------------------------------------------------
Ran 148 tests in 1.347s

OK
```
