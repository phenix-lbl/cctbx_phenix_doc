from django.shortcuts import render
from django.http import HttpResponse


def index(request):
  return render(request, 'tutorials_cctbx/index.html')
  #return HttpResponse("Hello, world. You're at the polls index.")

def about(request):
  return render(request, 'tutorials_cctbx/about.html')

def installation(request):
  return render(request, 'tutorials_cctbx/installation.html')

def cctbx_tour(request):
  return render(request, 'tutorials_cctbx/cctbx_tour.html')

def tutorials(request):
  args = {'is_active': 'display: block;'}
  return render(request, 'tutorials_cctbx/tutorials/tutorials_intro.html', args)

def tuto_melk_2019(request):
  args = {'is_active': 'display: block;'}
  return render(request, 'tutorials_cctbx/tutorials/tuto_melk_2019.html', args)

def tuto_rigid_body(request):
  args = {'is_active': 'display: block;'}
  return render(request, 'tutorials_cctbx/tutorials/tuto_rigid_body.html', args)

# ------------------------------------------------------------------------------

def documentation_overview(request):
  args = {'is_active_doc': 'display: block;'}
  return render(request, 'tutorials_cctbx/documentation/documentation_overview.html', args)

def doc_flex_array(request):
  args = {'is_active_doc': 'display: block;'}
  return render(request, 'tutorials_cctbx/documentation/doc_flex_array.html', args)

def doc_phil(request):
  args = {'is_active_doc': 'display: block;'}
  return render(request, 'tutorials_cctbx/documentation/doc_phil.html', args)

def doc_high_level_objects(request):
  args = {'is_active_doc': 'display: block;'}
  return render(request, 'tutorials_cctbx/documentation/doc_high_level_objects.html', args)

def doc_data_manager(request):
  args = {'is_active_doc': 'display: block;'}
  return render(request, 'tutorials_cctbx/documentation/doc_data_manager.html', args)

def doc_model_manager(request):
  return render(request, 'tutorials_cctbx/documentation/doc_model_manager.html')

def doc_map_manager(request):
  return render(request, 'tutorials_cctbx/documentation/doc_map_manager.html')

def doc_model_map_manager(request):
  return render(request, 'tutorials_cctbx/documentation/doc_model_map_manager.html')

# ------------------------------------------------------------------------------

def getting_started(request):
  args = {'is_active_doc': 'display: block;'}
  return render(request, 'tutorials_cctbx/documentation/getting_started.html', args)

def newsletter_artcls(request):
  return render(request, 'tutorials_cctbx/newsletter_artcls.html')


def test(request):
  return render(request, 'tutorials_cctbx/test.html')

