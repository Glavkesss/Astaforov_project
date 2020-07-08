from django.shortcuts import render

# Create your views here.


def main_page(request):
    return render(request, 'portfolio/main_page.html')





def projects(request):
    return render(request, 'portfolio/my_projects.html')