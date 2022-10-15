from django.shortcuts import render
from django.http import HttpResponse
from Registration.models import Course,Batch,Student

# Create your views here.
def index(Request):
    return HttpResponse("<center><h1>Welcome to Prime Intuit Registration page</h1>")

def Home(Request):

#    return HttpResponse("<center><h1>Welcome to Prime Intuit home page</h1>")
 #   my_dict = {'Insert_Me': "I am a text from Registration/views.py"}
    batch_list= Batch.objects.order_by('batch_ID')
  #  batch_list= Batch.objects.raw('select * from Registration')
    data_dict= {'access_record':batch_list,'Insert_Me': "I am a text from Registration/views.py"}
    return render(Request, 'Registration/index.html',context=data_dict)