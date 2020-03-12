from django.shortcuts import render
from django.http import HttpResponse


def index(request):
  return render(request, 'tutorials_cctbx/index.html')
  #return HttpResponse("Hello, world. You're at the polls index.")

def download(request):
  return render(request, 'tutorials_cctbx/download.html')

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

def documentation_overview(request):
  args = {'is_active_doc': 'display: block;'}
  return render(request, 'tutorials_cctbx/documentation/documentation_overview.html', args)

def flex_array(request):
  args = {'is_active_doc': 'display: block;'}
  return render(request, 'tutorials_cctbx/documentation/flex_array.html', args)

def newsletter_artcls(request):
  return render(request, 'tutorials_cctbx/newsletter_artcls.html')

