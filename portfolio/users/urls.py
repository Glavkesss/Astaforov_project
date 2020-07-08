from django.urls import path
from .views import users_contacts

urlpatterns = [
    path('', users_contacts)
]