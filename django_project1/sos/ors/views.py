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

def test_list(request):
    list=[
        {'id':1,'first_name':"rahul","last_name":"patel","email":"rahul@gamil.com","password":"rahul@123"},
        {'id': 2, 'first_name': "amit", "last_name": "birla", "email": "amit@gamil.com", "password": "amit@123"},
        {'id': 3, 'first_name': "neha", "last_name": "sen", "email": "neha@gamil.com", "password": "neha@123"},
        {'id': 4, 'first_name': "puja", "last_name": "patidar", "email": "puja@gamil.com", "password": "puja@123"},
        {'id': 5, 'first_name': "aarya", "last_name": "varma", "email": "aarya@gamil.com", "password": "aarya@123"}
    ]
    return render(request,'test_list.html', {"list": list})

def user_list(request):
    form={}
    form['page_no'] = 1
    form['page_size'] = 5

    if request.method == 'POST':
        if request.POST['operation'] == "next":
            form['page_no'] = int(request.POST.get('pageNo'))
            form['page_no'] += 1

        if request.POST['operation'] == "previous" :
            form['page_no'] = int(request.POST.get('pageNo'))
            form['page_no'] -= 1

        if request.POST['operation'] == 'search':
            form['page_no'] = 1
            form['first_name'] = request.POST.get('firstName')

    service = UserService()
    list = service.search(form)
    index = (form['page_no'] - 1) * 5
    return render(request, "user_list.html", {"list": list,'page_no':form['page_no'], 'index': index})

def user_delete(request,id=0):
    service=UserService()
    service.delete(id)
    return redirect('/ors/list/')

def user_save(request):

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
    return render(request, 'user.html')

