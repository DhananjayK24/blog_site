from django.shortcuts import render
import logging

# Create your views here.

def starting_page(request):
    return render(request, "blog/index.html")

def individual_posts(request):
    return render(request, "blog/all-posts.html")

def detail_post(request):
    pass