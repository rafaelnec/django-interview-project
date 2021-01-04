from interview.tests.base import BaseTest
from django.test import Client

class Example(BaseTest):
    def setUp(self):
        self.c = Client()

    def test_main(self):
        response = self.c.get('/')
        self.assertEqual(response.status_code, 200)