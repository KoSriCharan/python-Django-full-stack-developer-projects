from django.shortcuts import render
from django.http import HttpResponse
from basicapp import forms
from basicapp.models import User

# Create your views here.
def index(request):
    return render(request, 'basicapp/index.html')

def form_name_view(request):
    form = forms.FormName()
    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            # Do something code
            print("Validation Success!")
            print("Name: " + form.cleaned_data['name'])
            print("Email: " + form.cleaned_data['email'])
            print("Text: " + form.cleaned_data['text'])

    return render(request, 'basicapp/form_page.html', {'form': form} )

def users(request):
    form = forms.NewUser()
    if request.method == 'POST':
        form = forms.NewUser(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("Error form invalid")
    
    return render(request, 'basicapp/users.html', {'form': form} )