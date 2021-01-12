import requests
import json


def get_resource(id=None):
    data = {

    }
    if data is not None:
        data = {

            'id': id
        }

    resp = requests.get('http://127.0.0.1:8000/student_basic/api2/', data=json.dumps(data))
    print(resp.json())


get_resource(10080)

#
# def create_resource():
#     new_data = {
#
#         'student_name': 'bharat',
#         'student_id': 10083,
#         'student_school': 'Xaviers',
#     }
#     resp = requests.post('http://127.0.0.1:8000/student_basic/api/', data=json.dumps(new_data))
#     print(resp.status_code)
#     print(resp.json())
#
#
# create_resource()

# def create_resource():
#     new_data = {
#
#         'active_backlogs': 11,
#         'B_id': 10093,
#     }
#     resp = requests.post('http://127.0.0.1:8000/student_basic/api2/', data=json.dumps(new_data))
#     print(resp.status_code)
#     print(resp.json())
#
#
# create_resource()


# # #
# def update_resource(id):
#     data = {
#         'active_backlogs': 20,
#         'id': id,
#     }
#     resp = requests.put('http://127.0.0.1:8000/student_basic/api2/', data=json.dumps(data))
#     print(resp.status_code)
#     print(resp.json())
#
#
# #
# #
# update_resource(10080)
# #
# def delete_resource(id):
#     data = {
#
#         'id': id,
#     }
#     resp = requests.delete('http://127.0.0.1:8000/student_basic/api2/', data=json.dumps(data))
#     print(resp.status_code)
#     print(resp.json())
#
#
# delete_resource(10090)


# def active_resource():
#     resp = requests.get('http://127.0.0.1:8000/student_basic/at_least/')
#     print(resp.status_code)
#     print(resp.json())
#
#
# active_resource()
