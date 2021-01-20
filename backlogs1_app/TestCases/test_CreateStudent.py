import json
import requests
import pytest


def test_create_new_student():
    new_data = {

        'student_name': 'Raj',
        'student_id': 10010,
        'student_school': 'Xaviers',
    }

    resp = requests.post('http://127.0.0.1:8000/student_basic/api/', data=json.dumps(new_data))
    assert resp.status_code == 201, "Data created"
    print(resp.headers.get('Content-Length'))


def test_create_existing_student():
    new_data = {

        'student_name': 'bharat',
        'student_id': 10096,
        'student_school': 'Xaviers',
    }

    resp = requests.post('http://127.0.0.1:8000/student_basic/api/', data=json.dumps(new_data))
    assert resp.status_code == 201, "Data already there "
    print(resp.headers.get('Content-Length'))
