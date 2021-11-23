from django.shortcuts import render
from django.http import HttpResponse

# ------------------------------------------------------------------------------

def index(request):
  return render(request, 'phenix/index.html')
  #return HttpResponse("Hello, world. You're at the index.")

# ------------------------------------------------------------------------------

def installation(request):
  return render(request, 'phenix/documentation/installation.html')

# ------------------------------------------------------------------------------

def overview(request):
  return render(request, 'phenix/documentation/overview.html')

def doc_quick_reference(request):
  return render(request, 'phenix/documentation/phenix_dev_doc_html/doc_quick_reference.html')

def directory_structure(request):
  return render(request, 'phenix/directory_structure.html')

# ------------------------------------------------------------------------------

def doc_mb_intro(request):
  return render(request, 'phenix/documentation/doc_mb_intro.html')

def doc_mb_read_files(request):
  return render(request, 'phenix/documentation/phenix_dev_doc_html/doc_mb_read_files.html')

def doc_mb_fit_ligand(request):
  return render(request, 'phenix/documentation/phenix_dev_doc_html/doc_mb_fit_ligand.html')

def doc_mb_model_building(request):
  return render(request, 'phenix/documentation/phenix_dev_doc_html/doc_mb_model_building.html')

def doc_mb_loop_fitting(request):
  return render(request, 'phenix/documentation/phenix_dev_doc_html/doc_mb_loop_fitting.html')

def doc_mb_replace_segment(request):
  return render(request, 'phenix/documentation/phenix_dev_doc_html/doc_mb_replace_segment.html')

def doc_mb_morphing(request):
  return render(request, 'phenix/documentation/phenix_dev_doc_html/doc_mb_morphing.html')

def doc_mb_sequence(request):
  return render(request, 'phenix/documentation/phenix_dev_doc_html/doc_mb_sequence.html')

# ------------------------------------------------------------------------------


def restraint_jiffys(request):
  return render(request, 'phenix/restraint_jiffys.html')

def prog_program_template(request):
  return render(request, 'phenix/programming/prog_program_template.html')

def prog_runsnake(request):
  return render(request, 'phenix/programming/prog_runsnake.html')

def prog_lineprofiler(request):
  return render(request, 'phenix/programming/prog_lineprofiler.html')

# ------------------------------------------------------------------------------


def template(request):
  return render(request, 'phenix/documentation/phenix_dev_doc_html/template.html')


