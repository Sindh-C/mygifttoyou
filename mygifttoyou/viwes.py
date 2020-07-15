from django.shortcuts import render#(print data)

# Create your views here.
#create with html response
from django.http import HttpResponse
def index(request):
	return HttpResponse("hello world")#htmlstatment (html statement as an argument)
def home(request):
    	return HttpResponse("Welcome to dijango page!!!!!")#htmlstatment (html statement as an argument)

