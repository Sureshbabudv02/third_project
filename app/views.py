from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def interviewer(request):
    return HttpResponse('<h1><marquee>Hi Musician! How many years of Experience do you have in Music?</h1></marquee>')

def musician(request):
    return HttpResponse('<h1><marquee>Hi! I have 10 years of Experience in Music</h1></marquee>')
