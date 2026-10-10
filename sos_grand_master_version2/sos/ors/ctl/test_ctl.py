from django.shortcuts import render, redirect
from .base_ctl import BaseCtl

from ..service.role_service import RoleService
from ..service.user_service import UserService
from ..utility.html_utility import HtmlUtility


class TestCtl(BaseCtl):

    def request_to_form(self, request):
        self.form['role_id'] = request.POST.get('roleId','')
        self.form['gender'] = request.POST.get('gender','')
        self.form['user_id'] = request.POST.get('userId','')

    def preload(self, request):
        gender_list = ["Male", "Female"]
        role_list = RoleService().search({})
        user_list = UserService().search({})
        self.preload_data['gender_select'] = HtmlUtility.get_list_from_list(
            "gender",
            self.form.get(""),
            gender_list
        )
        self.preload_data["role_select"] = HtmlUtility.get_list_from_beans(
            "roleId",
            int(self.form.get("role_id") or 0),
            role_list
        )
        self.preload_data["user_select"] = HtmlUtility.get_list_from_beans(
            "userId",
            int(self.form.get("id") or 0),
            user_list

        )
        return self.preload_data

    def display(self,request,params={}):

        return render(request, 'test.html', {'form': self.form, "preload_data": self.preload(request)})

    def submit(self,request,params={}):

        if request.POST.get('operation','') == "signin":

              return render(request, 'test.html', {'form': self.form, "preload_data": self.preload(request)})


