from django.shortcuts import render

from ..service.forget_password_service import ForgetPasswordService
from ..utility.data_validator import DataValidator
from .base_ctl import BaseCtl


class ForgetPasswordCtl(BaseCtl):

    def input_validation(self, request):
        input_error = self.form.get('input_error', {})
        input_error['error'] = False

        if DataValidator.is_null(request.POST.get('loginId', '')):
            input_error['login_id'] = 'Login ID is required'
            input_error['error'] = True

        return input_error['error']

    def request_to_form(self, request):
        self.form['login_id'] = request.POST.get('loginId', '')

    def display(self, request, params={}):
        return render(request, self.get_template(), {'form': self.form})

    def submit(self, request, params={}):
        try:
            user = self.get_service().forget_password(self.form['login_id'])
            self.form['error'] = False
            self.form['message'] = 'your password is ' + str(user.password)
        except Exception as e:
            self.form['message'] = str(e)
            self.form['error'] = True

        return render(request, self.get_template(), {'form': self.form})

    def get_template(self):
        return 'forget_password.html'

    def get_service(self):
        return ForgetPasswordService()
