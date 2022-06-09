# Optibrium Technical Test - A Collection of People

- **Solution by**: *Ryan Gilchrist*
- **Date**: *9th June, 2020*
- [Endpoint specification](https://github.com/optibrium/python_developer_tech_test/blob/main/People.md)
 
### Requirements

The API was developed using `Python v3.9.13`, although `v3.8` or above is likely to work. Additional requirements are `Flask` and `requests` (`pip install -r requirements.txt` in a fresh virtual environment).

### Files

- `app.py`: Flask application. `python app.py` will start the server on https://127.0.0.1:5000/.
- `tests.py`: Unit tests for the application. `python -m unittest tests.py`. Note that the server must be running for tests to work.
- `database.py`: Modified version of the [original file](https://github.com/optibrium/python_developer_tech_test/blob/main/database.py) from Optibrium.
- `requirements.txt`: Environment requirements; use with `pip`.

### Development timeline

1. 'Skeleton draft' of API routes.
2. Implement successful response codes.
3. Implement failed response codes that don't require interacting with the SQL database.
4. Link with SQL database and pass appropriate json responses.
5. Define 'server inactive' criteria (in this case, if the file doesn't exist) and implement active/inactive responses.

### Approach to testing

I used a Test-Driven-Development (TDD) approach and commited frequently. This had several benefits:
- I changed the implementation a few times (e.g., by creating a few new functions). The TDD approach removes the obstacle of implementation-specific tests, which makes refactoring more difficult.
- I am by no means an expert on using Flask or sqlite3. The TDD approach encouraged me to think about the problem in small steps and allowed me to develop a solution using methods I am less familiar with.
- Every line of the code is accounted for with a test of some description (as I only wrote code required to pass something in `tests.py`), and so the code hasn't been over-engineered.

**[TODO also test API works when using curl this evening]**

### What could be done better?

- Better criteria for inactive database.
- More tests?
- (In theory) Think about how the API would scale up.
