from django.http import HttpResponse
from django.shortcuts import render,redirect

from .service.user_service import UserService


def test_ors(request):
    return HttpResponse('<h1> what are you doing </h1>')

def welcome(request):
    return render(request,'welcome.html')

def user_signin(request):
    message=''
    if request.method=='POST':
        form={}
        form['login_id']=request.POST.get("loginId")
        form['password']=request.POST.get("password")

        service=UserService()
        records=service.authenticate(form['login_id'],form['password'])

        if len(records)>0:
            request.session['first_name'] = records[0].get('first_name')
            return  render(request,'welcome.html')
        else:
            message='loginid & password invalid'


    return render(request,'login.html',{'message': message})


def user_signup(request):

    if request.method == "POST":
        form = {}
        form['first_name'] = request.POST.get('firstName')
        form['last_name'] = request.POST.get('lastName')
        form['login_id'] = request.POST.get('loginId')
        form['password'] = request.POST.get('password')
        form['dob'] = request.POST.get('dob')
        form['address'] = request.POST.get('address')

        service =UserService()
        service.add(form)
    return render(request, 'registration.html')

def user_logout(request):
    request.session['first_name'] = None
    return redirect('/ors/signin/')