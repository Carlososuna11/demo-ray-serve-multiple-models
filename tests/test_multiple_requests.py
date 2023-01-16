from unittest import TestCase
from functools import partial
import multiprocessing
import requests


def send_request(x, url, json):
    return requests.post(
        url,
        json=json,
    )


class TestMultipleRequests(TestCase):

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

        # send many requests to the API at the same time
        # multiprocessing

        responses = multiprocessing.Pool(2).map(
            partial(send_request, url=url, json=json),
            range(10)
        )

        # assert all responses are 200
        for response in responses:
            self.assertEqual(response.status_code, 200)

        # assert all responses are the same
        for response in responses:
            self.assertIsInstance(response.json(), list)

    def test_generation(self):
        url = self.url_base+"generation"
        json = {'text': self.request_text}

        # send many requests to the API at the same time
        # multiprocessing

        responses = multiprocessing.Pool(2).map(
            partial(send_request, url=url, json=json),
            range(10)
        )

        # assert all responses are 200
        for response in responses:
            self.assertEqual(response.status_code, 200)

        # assert all responses are the same
        for response in responses:
            self.assertIsInstance(response.json(), list)
