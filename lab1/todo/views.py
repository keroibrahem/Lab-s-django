from django.shortcuts import render, redirect
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect


# Create your views here.
def index(request):
    # res = HttpResponse("Welcome to the Todo Index Page!")
    # print(request.method)  # Print the request method to the console
    # print(request.path)  # Print the request method to the console
    # print(request.GET)  # Print the request method to the console
    # return res
    return render(request, 'base_layout.html' , {'title': 'Todo Index Page','content': 'Welcome to the Todo Index Page!'})