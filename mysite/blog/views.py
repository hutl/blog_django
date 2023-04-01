from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
def detail(request,post_id):
    return HttpResponse("teste" % post_id)