import unittest
import requests

BASE_URL = "http://127.0.0.1:5000/"
HEADER = {"x-api-key": "skeleton-key"}


class GetPeopleTests(unittest.TestCase):

    def test_success(self):
        response = requests.get(BASE_URL + "person", headers=HEADER)
        self.assertEqual(response.status_code, 200)

    def test_notoken(self):
        response = requests.get(BASE_URL + "person")
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json(), {"error": "Authorization required"})


class PostPersonTests(unittest.TestCase):

    def test_success(self):
        response = requests.post(BASE_URL + "person", headers=HEADER, json={"name": "Ryan"})
        self.assertEqual(response.status_code, 201)

    def test_notoken(self):
        response = requests.post(BASE_URL + "person", json={"name": "Ryan"})
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json(), {"error": "Unauthorised"})

    def test_alphanumeric(self):
        response = requests.post(BASE_URL + "person", headers=HEADER, json={"name": "Ryan!"})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"error": "Names must be alphanumeric"})


class DeletePersonTests(unittest.TestCase):

    def test_success(self):
        response = requests.delete(BASE_URL + "person/1", headers=HEADER)
        self.assertEqual(response.status_code, 204)

    def test_notoken(self):
        response = requests.delete(BASE_URL + "person/1")
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json(), {"error": "Unauthorised"})


class GetStatusTests(unittest.TestCase):

    def test_success(self):
        response = requests.get(BASE_URL + "status")
        self.assertEqual(response.status_code, 200)
