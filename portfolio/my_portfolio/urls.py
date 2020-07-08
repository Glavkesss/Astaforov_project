from django.contrib import admin
from django.urls import path, include
from my_portfolio.views import main_page as M, projects as P

urlpatterns = [
    path('', M),
    path('all_projects/', P),
    ]