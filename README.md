# Optibrium Technical Test - A Collection of People

- **Solution by**: *Ryan Gilchrist*
- **Date**: *9th June, 2020*
- [Endpoint specification](https://github.com/optibrium/python_developer_tech_test/blob/main/People.md)
 
### Requirements

The API was developed using `Python v3.9.13`. Additional requirements include `Flask` and `requests`. Install these with `pip install -r requirements.txt` in a fresh virtual environment.

### Files

- `app.py`: Flask application. `python app.py` will start the server on https://127.0.0.1:5000/.
- `tests.py`: Unit tests for the application. `python -m unittest tests.py` will run these tests. The server must be running for the tests to work.
- `database.py`: Modified version of the [original file](https://github.com/optibrium/python_developer_tech_test/blob/main/database.py) from Optibrium.
- `requirements.txt`: Environment requirements. Install using `pip`.

### Development timeline

1. 'Skeleton draft' of API routes.
2. Implement successful response codes.
3. Implement failed response codes that don't require logic that involves interacting with the SQL database.
4. Link with SQL database and pass appropriate json responses.
5. Implement remaining failed response codes.
6. Define the 'server inactive' criteria (defined in this project as to whether the file exists) and implement relevant responses.

### Additional feature included

When trying to `POST` without a `name` key, the API will return `status_code 410` with response of `{"error": "'name' is not specified"}`. This is not part of the original specification, but adds robustness to the server.

### Approach to testing

I used Test-Driven-Development (TDD) and commited frequently. The benefits of this were:
- I changed the implementation a few times (e.g., by creating a few new functions and classes). TDD discourages implementation-specific tests, which provides more freedom to refactor.
- I am by no means an expert on using Flask or sqlite3. TDD encouraged me to think about the problem in small steps, allowing me to develop a solution using methods I am less familiar with.
- Every line of `app.py` is accounted for with a test of some description (as I only wrote code required to pass something in `tests.py`), and so the code hasn't been over-engineered.

The API was also tested using curl and by sending a range of requests in Python.

### What could be done better?

- Better criteria for inactive database.
- More tests?
- Think about how the API would scale up to many users.
