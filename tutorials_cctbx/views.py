from django.shortcuts import render
from django.http import HttpResponse


def index(request):
  return render(request, 'tutorials_cctbx/index.html')
  #return HttpResponse("Hello, world. You're at the polls index.")

def tutorials(request):
  args = {'is_active': 'display: block;'}
  return render(request, 'tutorials_cctbx/tutorials/tutorials_intro.html', args)

def melk_2019_intro(request):
  args = {'is_active': 'display: block;'}
  return render(request, 'tutorials_cctbx/melk_2019/melk_2019_intro.html', args)

def flex_array(request):
  args = {'is_active_doc': 'display: block;'}
  return render(request, 'tutorials_cctbx/flex_array.html', args)

