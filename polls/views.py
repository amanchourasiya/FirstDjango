from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(response):
    return HttpResponse('Hey Got the first app running')

def detail(request,question_id):
    return HttpResponse("You are looking at question %s." % question_id)

def results(request,question_id):
    response = "you are looking at the response of question %s."
    return HttpResponse(response % question_id)

def vote(request,question_id):
    return HttpResponse("You are voting on question %s." % question_id)
