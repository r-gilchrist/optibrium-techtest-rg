import unittest
import requests
import os
from database import ensure_tables_are_created

BASE_URL = "http://127.0.0.1:5000/"
HEADER = {"x-api-key": "skeleton-key"}


def get(endpoint="person", authenticate=True):
    '''Sends GET request'''
    headers = HEADER if authenticate else {}
    response = requests.get(BASE_URL + endpoint, headers=headers)
    return response


def post(name="Ryan", authenticate=True):
    '''Sends POST request'''
    headers = HEADER if authenticate else {}
    response = requests.post(BASE_URL + "person", headers=headers, json={"name": name})
    return response


def delete(id=1, authenticate=True):
    '''Sends DELETE request'''
    headers = HEADER if authenticate else {}
    response = requests.delete(BASE_URL + f"person/{id}", headers=headers)
    return response


class GetPeopleTests(unittest.TestCase):
    '''Tests for expected GET functionality'''

    def setUp(self):
        '''Reset the table for each test'''
        if os.path.exists(db := "database.db"):
            os.remove(db)
        ensure_tables_are_created()

    def test_success_one(self):
        post()
        response = get()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"1": {"name": "Ryan"}})

    def test_success_two(self):
        post()
        post(name="Sarah")
        response = get()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"1": {"name": "Ryan"}, "2": {"name": "Sarah"}})

    def test_notoken(self):
        response = get(authenticate=False)
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json(), {"error": "Authorization required"})


class PostPersonTests(unittest.TestCase):
    '''Tests for expected POST functionality'''

    def setUp(self):
        '''Reset the table for each test'''
        if os.path.exists(db := "database.db"):
            os.remove(db)
        ensure_tables_are_created()

    def test_success(self):
        response = post()
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(), {"id": 1, "name": "Ryan"})

    def test_notoken(self):
        response = post(authenticate=False)
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json(), {"error": "Unauthorised"})

    def test_alphanumeric(self):
        response = post(name="Ryan!!!")
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"error": "Names must be alphanumeric"})

    def test_duplicate(self):
        post()
        response = post()
        self.assertEqual(response.status_code, 409)
        self.assertEqual(response.json(), {"error": "Name exists"})

    def test_badjson(self):
        response = requests.post(BASE_URL + "person", headers=HEADER, json={"bad_param": "Ryan"})
        self.assertEqual(response.status_code, 410)
        self.assertEqual(response.json(), {"error": "'name' is not specified"})


class DeletePersonTests(unittest.TestCase):
    '''Tests for expected DELETE functionality'''

    def setUp(self):
        '''Reset the table for each test'''
        if os.path.exists(db := "database.db"):
            os.remove(db)
        ensure_tables_are_created()
        post()

    def test_success(self):
        response = delete()
        self.assertEqual(response.status_code, 204)

    def test_notoken(self):
        response = delete(authenticate=False)
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json(), {"error": "Unauthorised"})

    def test_notfound(self):
        response = delete(id=100)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json(), {"error": "Not Found"})


class GetStatusTests(unittest.TestCase):
    '''Tests for expected status endpoint functionality'''

    def setUp(self):
        ensure_tables_are_created()

    def test_success(self):
        response = get(endpoint='status', authenticate=False)  # No authentication required
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"msg": "OK"})

    def test_offline(self):
        os.remove("database.db")
        response = get(endpoint='status', authenticate=False)  # No authentication required
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json(), {"error": "Database is not active"})


class DeleteDatabaseTests(unittest.TestCase):
    '''Tests for expected functionality when database is deleted from disk'''

    def setUp(self):
        if os.path.exists(db := "database.db"):
            os.remove(db)

    def test_get(self):
        response = get()
        self.assertEqual(response.status_code, 200)

    def test_post(self):
        response = post()
        self.assertEqual(response.status_code, 201)

    def test_delete(self):
        post()
        response = delete()
        self.assertEqual(response.status_code, 204)

    def post_and_get(self):
        post()
        response = get()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"id": 1, "name": "Ryan"})
