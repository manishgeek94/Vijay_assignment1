import json
import requests


def test_atleast_one_active_backlog():
    resp = requests.get('http://127.0.0.1:8000/student_basic/at_least/')
    assert resp.status_code == 200


def test_no_active_backlog():
    resp = requests.get('http://127.0.0.1:8000/student_basic/at_least/')
    assert resp.status_code == 404
