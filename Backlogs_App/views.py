from django.shortcuts import render, HttpResponse
from .models import Student, Backlogs
from django.views.generic import View
from django.core.serializers import serialize
import json
from .mixins import SerializeMixin
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .forms import StudentForm
import logging


@method_decorator(csrf_exempt, name='dispatch')
class Student_data(View, SerializeMixin):
    def get_student_by_id(self, id):
        try:
            student_info = Student.objects.get(student_id=id)
        except Student.DoesNotExist:
            student_info = None
        return student_info

    def get(self, request, *args, **kwargs):
        logging.basicConfig(filename='Logging/get_info.txt', level=logging.info())
        data = request.body
        p_data = json.loads(data)
        student_id = p_data.get('id', None)
        if student_id is not None:
            # stud_obj = self.get_student_by_id(student_id)
            stud_obj = Student.objects.get(student_id=student_id)
            print(type(stud_obj))
            if stud_obj is None:
                return logging.info(HttpResponse(json.dumps({'msg': 'student id not available in our system'}),
                                                 content_type='application/json'))
            json_data = serialize('json', stud_obj)
            # json_data = serialize('json', stud_obj)
            # json_data = serialize('json', qs)
            print(json_data)
            return HttpResponse(json_data, content_type='application/json')

        qs = Student.objects.all()
        print(qs)
        json_data = serialize('json', qs)
        print(json_data)
        return HttpResponse(json_data, content_type='application/json')

    def post(self, request, *args, **kwargs):
        # logging.basicConfig(filename='create_info.txt')
        data = request.body
        p_data = json.loads(data)
        form = StudentForm(p_data)
        if form.is_valid():
            obj = form.save(commit=True)
            logging.error('Student added successfully')
            return HttpResponse(json.dumps({'msg': 'Student added successfully'}))
        if form.errors:
            json_data = json.dumps(form.errors)
            return HttpResponse(json_data, content_type='application/json')

    def put(self, request, *args, **kwargs):
        data = request.body
        p_data = json.loads(data)
        student_id = p_data.get('id', None)
        if student_id is not None:
            stud_obj = self.get_student_by_id(student_id)
            if stud_obj is None:
                return HttpResponse(json.dumps({'msg': 'Student id not available in our system'}),
                                    content_type='application/json')
            new_student = p_data

            old_student = {
                'student_name': stud_obj.student_name,
                'student_id': stud_obj.student_id,
                'student_school': stud_obj.student_school,

            }

            old_student.update(new_student)
            form = StudentForm(old_student, instance=stud_obj)
            if form.is_valid():
                form.save(commit=True)
                return HttpResponse(json.dumps({'msg': 'Updated successfully'}))
            if form.errors:
                json_data = json.dumps(form.errors)
                return HttpResponse(json_data)

    def delete(self, request, *args, **kwargs):
        data = request.body
        print(data)
        p_data = json.loads(data)
        student_id = p_data.get('id', None)
        if student_id is not None:
            stud_obj = self.get_student_by_id(student_id)
            if stud_obj is None:
                return HttpResponse(json.dumps({'msg': 'Student id not available in our system'}),
                                    content_type='application/json')
            status, deleted_item = stud_obj.delete()
            if status == 1:
                return HttpResponse(json.dumps({'msg': 'deleted successfully'}))
            return HttpResponse(json.dumps({'msg': 'some issue occured ,try again'}))
