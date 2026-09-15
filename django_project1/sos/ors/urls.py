
from django.urls import path
from .  import views

urlpatterns=[
    path('test_ors/',views.test_ors),
    path('welcome/',views.welcome),
    path('signin/',views.user_signin),
    path('signup/',views.user_signup),
    path('logout/', views.user_logout),
    path('testlist/',views.test_list),
    path('list/',views.user_list),
    path('',views.welcome)
]
