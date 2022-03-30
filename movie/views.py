from unittest import result
from django.shortcuts import render
from django.http import HttpResponse
from .request import get_movies, search_movie

# Create your views here.

def index(request):
    movies = get_movies('popular')

    
    
    return render(request, 'index.html',{'movies':movies})

# def search(request):
#     if 'title' in request.GET and request.GET["title"]:
#         mname = request.GET.get('title')
#         result = search_movie('mname')
#         message = f"{mname}"
#         for i in result:
#             print(i)
        
#         return render(request, 'search.html',{'movies':result,'message':message})
        
#     else:
#         message = 'no movie'
#         return render(request, 'search.html',{'message':message})
    
    





