from django.urls import path
from . import views

urlpatterns = [
    path('display/',views.test_ors),
    path('welcome/',views.welcome),
    path('signin/',views.user_signin),
    path('signup/',views.user_signup),
    path('logout/',views.user_logout),
    path('testlist/',views.test_list),
    path('list/',views.user_list),
    path('delete/<int:id>/',views.user_delete),
    path('edit/<int:id>/', views.edit_user),
    path('save/',views.user_save),
    path('',views.welcome),

]
