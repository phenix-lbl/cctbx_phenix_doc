from django.shortcuts import render
from django.http import HttpResponse

def index(request):
  return render(request, 'phenix/index.html')
  #return HttpResponse("Hello, world. You're at the index.")

def installation(request):
  return render(request, 'phenix/installation.html')

def doc_overview(request):
  return render(request, 'phenix/doc_overview.html')

def examples(request):
  return render(request, 'phenix/examples.html')

def template(request):
  return render(request, 'phenix/documentation/template.html')
