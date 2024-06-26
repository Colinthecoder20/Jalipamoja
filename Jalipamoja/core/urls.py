from django.contrib.auth import views as auth_views
from django.urls import path

from . import views
from .forms import LoginForm, LogoutForm



from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='views'),
    path('contact/', views.contact, name='contact'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html',authentication_form=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='core/logout.html'), name='logout'),
]