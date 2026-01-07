from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic, Webpage, AccessRecord

# Create your views here.
def index(request):
    my_dict = {'insert_me': "Hello I am from first_app/view.py!"}
    return render(request, 'first_app/index.html', context=my_dict)    

def home(request):
    return HttpResponse("<strong>This is the home page of the First App.</strong>")

def help(request):
    my_dict = {'insert_me': "Hello I am from first_app/view.py's help function!"}
    return render(request, 'project_2app/help.html', context=my_dict)

def accessrecord(request):
    accessrecord_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': accessrecord_list}
    return render(request, 'first_app/accessrecord_list.html', context=date_dict)

def webpages(request):
    webpages_list = Webpage.objects.order_by(Topic)
    return render(request, )

