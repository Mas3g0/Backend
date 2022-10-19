from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.
def productView(request):
    html = "Welcome to my product page"
    return HttpResponse(html)

# Class based views.
class Myviews(View):
    def get(self,request):
        return HttpResponse("<h1>This is class based view</h1>")