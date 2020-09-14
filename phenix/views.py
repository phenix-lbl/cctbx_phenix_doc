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

def doc_high_level_model_building_intro(request):
  return render(request, 'phenix/documentation/doc_high_level_model_building_intro.html')

def doc_model_building_read_files(request):
  return render(request, 'phenix/documentation/doc_model_building_read_files.html')

def doc_fit_ligand(request):
  return render(request, 'phenix/documentation/doc_fit_ligand.html')

def doc_model_building_1(request):
  return render(request, 'phenix/documentation/doc_model_building_1.html')

def doc_model_building_2(request):
  return render(request, 'phenix/documentation/doc_model_building_2.html')

def doc_model_building_segment(request):
  return render(request, 'phenix/documentation/doc_model_building_segment.html')




