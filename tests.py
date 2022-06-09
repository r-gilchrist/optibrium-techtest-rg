import unittest
import requests
import os
from database import ensure_tables_are_created

BASE_URL = "http://127.0.0.1:5000/"
HEADER = {"x-api-key": "skeleton-key"}


class GetPeopleTests(unittest.TestCase):

    def setUp(self):
        '''Reset the table for each test'''
        if os.path.exists(db := "database.db"):
            os.remove(db)
        ensure_tables_are_created()

    def test_success_one(self):
        response = requests.post(BASE_URL + "person", headers=HEADER, json={"name": "Ryan"})
        response = requests.get(BASE_URL + "person", headers=HEADER)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"1": {"name": "Ryan"}})

    def test_success_two(self):
        response = requests.post(BASE_URL + "person", headers=HEADER, json={"name": "Ryan"})
        response = requests.post(BASE_URL + "person", headers=HEADER, json={"name": "Sarah"})
        response = requests.get(BASE_URL + "person", headers=HEADER)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"1": {"name": "Ryan"}, "2": {"name": "Sarah"}})

    def test_notoken(self):
        response = requests.get(BASE_URL + "person")
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json(), {"error": "Authorization required"})


class PostPersonTests(unittest.TestCase):

    def setUp(self):
        '''Reset the table for each test'''
        if os.path.exists(db := "database.db"):
            os.remove(db)
        ensure_tables_are_created()

    def test_success(self):
        response = requests.post(BASE_URL + "person", headers=HEADER, json={"name": "Ryan"})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(), {"id": 1, "name": "Ryan"})

    def test_notoken(self):
        response = requests.post(BASE_URL + "person", json={"name": "Ryan"})
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json(), {"error": "Unauthorised"})

    def test_alphanumeric(self):
        response = requests.post(BASE_URL + "person", headers=HEADER, json={"name": "Ryan!"})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"error": "Names must be alphanumeric"})

    def test_duplicate(self):
        for n in range(2):
            response = requests.post(BASE_URL + "person", headers=HEADER, json={"name": "Ryan"})
        self.assertEqual(response.status_code, 409)
        self.assertEqual(response.json(), {"error": "Name exists"})


class DeletePersonTests(unittest.TestCase):

    def setUp(self):
        '''Reset the table for each test'''
        if os.path.exists(db := "database.db"):
            os.remove(db)
        ensure_tables_are_created()
        requests.post(BASE_URL + "person", headers=HEADER, json={"name": "Ryan"})

    def test_success(self):
        response = requests.delete(BASE_URL + "person/1", headers=HEADER)
        self.assertEqual(response.status_code, 204)

    def test_notoken(self):
        response = requests.delete(BASE_URL + "person/1")
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json(), {"error": "Unauthorised"})

    def test_notfound(self):
        response = requests.delete(BASE_URL + "person/100", headers=HEADER)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json(), {"error": "Not Found"})


class GetStatusTests(unittest.TestCase):

    def test_success(self):
        response = requests.get(BASE_URL + "status")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"msg": "OK"})

    def test_offline(self):
        os.remove("database.db")
        response = requests.get(BASE_URL + "status")
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json(), {"error": "Database is not active"})
