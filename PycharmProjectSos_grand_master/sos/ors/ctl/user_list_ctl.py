from django.shortcuts import render,redirect

from ..service.user_service import UserService
from .base_ctl import BaseCtl


class UserListCtl(BaseCtl):

    def request_to_form(self,request):
       self.form['first_name'] = request.POST.get('firstName')

    def display(self,request,params ={}) :
        user_list = self.get_service().search(self.form)
        self.form['list'] = user_list
        return render(request, self.get_template(), {"form": self.form})

    def submit(self,request,param={}):
        if request.POST['operation'] == "next":
            self.form['page_no'] = int(request.POST.get('pageNo'))
            self.form['page_no'] += 1

        if request.POST['operation'] == "previous":
            self.form['page_no'] = int(request.POST.get('pageNo'))
            self.form['page_no'] -= 1

        if request.POST['operation'] == "search":
            self.form['page_no'] = 1
            self.request_to_form(request)

        user_list = self.get_service().search(self.form)
        self.form['list'] = user_list
        return render(request, self.get_template(), {"form": self.form})

    def get_template(self ):
        return 'user_list.html'
    def get_service(self):
        return UserService()
