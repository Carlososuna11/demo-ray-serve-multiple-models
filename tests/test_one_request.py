from unittest import TestCase
import requests


class TestOneRequests(TestCase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.url_base = "http://localhost:8000/"
        self.request_text = (
            "It was the best of times, it was"
            " the worst of times, it was the age "
            "of wisdom, it was the age of foolishness,"
            " it was the epoch of belief"
        )

    def test_summarization(self):
        url = self.url_base+"summarization"
        json = {'text': self.request_text}
        response = requests.post(
            url,
            json=json,
        )
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)

    def test_generation(self):
        url = self.url_base+"generation"
        json = {'text': self.request_text}
        response = requests.post(
            url,
            json=json,
        )
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)
