import unittest
import requests

BASE_URL = "http://127.0.0.1:5000/"


class GetPeopleTests(unittest.TestCase):

    def test_success(self):
        response = requests.get(BASE_URL + "person")
        self.assertEqual(response.status_code, 200)


class PostPersonTests(unittest.TestCase):

    def test_success(self):
        response = requests.post(BASE_URL + "person", json={"name": "Ryan"})
        self.assertEqual(response.status_code, 201)


class DeletePersonTests(unittest.TestCase):

    def test_success(self):
        response = requests.delete(BASE_URL + "person/1")
        self.assertEqual(response.status_code, 204)


class GetStatusTests(unittest.TestCase):

    def test_success(self):
        response = requests.get(BASE_URL + "status")
        self.assertEqual(response.status_code, 200)
