from django.shortcuts import render, redirect

from .base_ctl import BaseCtl
from ..models import Marksheet
from ..service.marksheet_service import MarksheetService
from ..service.student_service import StudentService
from ..utility.data_validator import DataValidator
from ..utility.html_utility import HtmlUtility


class MarksheetCtl(BaseCtl):

    def preload(self, request):
        student_list = StudentService().search({})

        self.form['preload_list'] = student_list
        self.preload_data['student_select'] = HtmlUtility.get_list_from_beans(
            "studentId",
            self.form.get("student_id"),
            student_list
        )
        return self.preload_data

    def input_validation(self, request):
        input_error = self.form.get("input_error")
        input_error['error'] = False

        if (DataValidator.is_null(request.POST.get("roll_number", ''))):
            input_error['roll_number'] = 'Roll_No is required'
            input_error['error'] = True
        if (DataValidator.is_null(request.POST.get("physics", ''))):
            input_error['Physics'] = 'Physics is required'
            input_error['error'] = True
        if (DataValidator.is_null(request.POST.get("chemistry", ''))):
            input_error['Chemistry'] = 'Chemistry is required'
            input_error['error'] = True
        if (DataValidator.is_null(request.POST.get("maths", ''))):
            input_error['Maths'] = 'Maths is required'
            input_error['error'] = True
        if (DataValidator.is_null(self.form['student_id']) or request.POST.get("studentId") == "0"):
            input_error['student_id'] = 'Student is required'
            input_error['error'] = True
        return input_error['error']

    def request_to_form(self, request):
        self.form['id'] = int(request.POST.get('id', 0))
        self.form['roll_number'] = request.POST.get('roll_number')
        self.form['Physics'] = request.POST.get('physics')
        self.form['Chemistry'] = request.POST.get('chemistry')
        self.form['Maths'] = request.POST.get('maths')
        self.form['student_id'] = int(request.POST.get('studentId', 0))

    def form_to_model(self, obj):
        obj.id = self.form['id']
        obj.roll_number  = self.form['roll_number']
        obj.physics = self.form['Physics']
        obj.chemistry = self.form['Chemistry']
        obj.maths = self.form['Maths']
        obj.student_id = int(self.form['student_id'])
        student = StudentService().get(self.form['student_id'])
        obj.student_name = student.first_name + " " + student.last_name
        return obj

    def model_to_form(self, obj):
        self.form['id'] = obj.id
        self.form['roll_number']=obj.roll_number
        self.form['Physics']=obj.physics
        self.form['Chemistry']=obj.chemistry
        self.form['Maths']=obj.maths
        self.form['student_id'] = obj.student_id
        self.form['student_name'] = obj.student_name

    def display(self, request, params={}):

        return render(request, self.get_template(), {'form': self.form, "preload_data": self.preload(request)})

    def submit(self, request, params={}):
        try:
            marksheet = self.form_to_model(Marksheet())
            self.get_service().save(marksheet)
            if self.form['id'] > 0:
                self.form['message'] = 'Marksheet Updated Successfully...!!!'
            else:
                self.form['message'] = 'Marksheet Added Successfully...!!!'
        except Exception as e:
            self.form['message'] = str(e)
            self.form['error'] = True
        return render(request, self.get_template(), {'form': self.form, "preload_data": self.preload(request)})

    def get_service(self):
        return MarksheetService()

    def get_template(self):
        return 'marksheet.html'
