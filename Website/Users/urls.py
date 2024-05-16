from django.urls import path
from . import views

app_name = 'Users'

urlpatterns = [
    path('signup/', views.sign_up, name='signup'),
]