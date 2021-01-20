import json
import requests


def test_update_student(id=10082):
    data = {
        'student_school': 'Army public school',
        'id': id,
    }
    resp = requests.put('http://127.0.0.1:8000/student_basic/api/', data=json.dumps(data))
    assert resp.status_code == 200


def test_update_unknown_id(id=100100):
    data = {
        'student_school': 'Army public school',
        'id': id,
    }
    resp = requests.put('http://127.0.0.1:8000/student_basic/api/', data=json.dumps(data))
    assert resp.status_code == 200
