from django.shortcuts import render
from django.http import HttpResponse

def index(request):
  return render(request, 'phenix/index.html')
  #return HttpResponse("Hello, world. You're at the index.")

def installation(request):
  return render(request, 'phenix/documentation/installation.html')

def doc_overview(request):
  return render(request, 'phenix/documentation/doc_overview.html')

def doc_quick_reference(request):
  return render(request, 'phenix/documentation/phenix_dev_doc_html/doc_quick_reference.html')

def examples(request):
  return render(request, 'phenix/examples.html')

def template(request):
  return render(request, 'phenix/documentation/phenix_dev_doc_html/template.html')

def doc_high_level_model_building_intro(request):
  return render(request, 'phenix/documentation/doc_high_level_model_building_intro.html')

def doc_model_building_read_files(request):
  return render(request, 'phenix/documentation/phenix_dev_doc_html/doc_model_building_read_files.html')

def doc_fit_ligand(request):
  return render(request, 'phenix/documentation/phenix_dev_doc_html/doc_fit_ligand.html')

def doc_model_building_1(request):
  return render(request, 'phenix/documentation/phenix_dev_doc_html/doc_model_building_1.html')

def doc_model_building_2(request):
  return render(request, 'phenix/documentation/phenix_dev_doc_html/doc_model_building_2.html')

def doc_model_building_3(request):
  return render(request, 'phenix/documentation/phenix_dev_doc_html/doc_model_building_3.html')

def doc_model_building_morphing(request):
  return render(request, 'phenix/documentation/phenix_dev_doc_html/doc_model_building_morphing.html')

def doc_model_building_sequence(request):
  return render(request, 'phenix/documentation/phenix_dev_doc_html/doc_model_building_sequence.html')

def doc_program_template(request):
  return render(request, 'phenix/documentation/phenix_dev_doc_html/doc_program_template.html')

def prog_overview(request):
  return render(request, 'phenix/programming/prog_overview.html')

def prog_runsnake(request):
  return render(request, 'phenix/programming/prog_runsnake.html')




