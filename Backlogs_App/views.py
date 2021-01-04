from django.shortcuts import render,HttpResponse
from .models import Student,Backlogs
from django.views.generic import View
from django.core.serializers import serialize
import json
from .utils import is_json
from .mixins import SerializeMixin
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .forms import StudentForm


@method_decorator(csrf_exempt, name='dispatch')
class Student_data(View, SerializeMixin):
    def get_student_by_id(self, id):
        try:
            student_info = Student.objects.get(student_id=id)
        except Student.DoesNotExist:
            student_info = None
        return student_info

    def get(self, request, *args, **kwargs):
        data = request.body
        valid_json = is_json(data)
        if not valid_json:
            return HttpResponse(json.dumps({'msg': 'Please send json data'}, indent=4), status=400)

        p_data = json.loads(data)
        student_id = p_data.get('id', None)
        if student_id is not None:
            stud_obj = self.get_student_by_id(student_id)
            if stud_obj is None:
                return HttpResponse(json.dumps({'msg': 'Product id not available in our system'}),
                                    content_type='application/json')
            json_data = self.serialize([stud_obj, ])
            return HttpResponse(json_data, content_type='application/json')

        qs = Student.objects.all()
        json_data = self.serialize(qs)
        return HttpResponse(json_data, content_type='application/json')

    def post(self, request, *args, **kwargs):
        data = request.body
        valid_json = is_json(data)
        if not valid_json:
            return HttpResponse(json.dumps({'msg': 'Please send json data'}), status=400)
        p_data = json.loads(data)
        form = StudentForm(p_data)
        if form.is_valid():
            obj = form.save(commit=True)
            return HttpResponse(json.dumps({'msg': 'Product added successfully'}))
        if form.errors:
            json_data = json.dumps(form.errors)
            return HttpResponse(json_data, content_type='application/json')

    def put(self, request, *args, **kwargs):
        data = request.body
        valid_json = is_json(data)
        if not valid_json:
            return HttpResponse(json.dumps({'msg': 'Please send json data'}, indent=4), status=400)

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
        valid_json = is_json(data)
        if not valid_json:
            return HttpResponse(json.dumps({'msg': 'Please send json data'}, indent=4), status=400)

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










