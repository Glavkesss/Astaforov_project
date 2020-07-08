from django.shortcuts import render
from .forms import UserForm

def users_contacts(request):
    ctx = {}
    ctx['form'] = UserForm()
    if request.method == 'GET':

        return render(request, 'users/index.html', ctx)

    elif request.method == 'POST':
        form = UserForm(request.POST)
        print('form ', form)
        if form.is_valid():
            print('cleaned data ', form.cleaned_data)
            form.save()
        return render(request, 'users/index.html', ctx)
