from django.shortcuts import render
from django.http import HttpResponse

args = {'collapse_state': ''}

#def index(request):
#  args = {'collapse_state': 'collapse'}
#  return render(request, 'tutorials_cctbx/index.html', args)
#  #return HttpResponse("Hello, world. You're at the polls index.")
#
#def melk_2019_1(request):
#  return render(request, 'tutorials_cctbx/melk_2019/melk_2019_1.html', args)
#
#def melk_2019_2(request):
#  return render(request, 'tutorials_cctbx/melk_2019/melk_2019_2.html', args)
#
#def melk_2019_3(request):
#  return render(request, 'tutorials_cctbx/melk_2019/melk_2019_3.html', args)
#
#def melk_2019_4(request):
#  return render(request, 'tutorials_cctbx/melk_2019/melk_2019_4.html', args)
#
#def melk_2019_5(request):
#  return render(request, 'tutorials_cctbx/melk_2019/melk_2019_5.html', args)
#
#def melk_2019_intro(request):
#  return render(request, 'tutorials_cctbx/melk_2019/melk_2019_intro.html', args)
#
#def flex_array(request):
#  args = {'collapse_state': 'collapse'}
#  return render(request, 'tutorials_cctbx/flex_array/flex_array.html', args)


def index(request):
  return render(request, 'tutorials_cctbx/index.html')
  #return HttpResponse("Hello, world. You're at the polls index.")

def tutorials(request):
  args = {'is_active': 'display: block;'}
  return render(request, 'tutorials_cctbx/tutorials.html', args)

def melk_2019_1(request):
  args = {'is_active': 'display: block;'}
  return render(request, 'tutorials_cctbx/melk_2019/melk_2019_1.html', args)

def melk_2019_2(request):
  return render(request, 'tutorials_cctbx/melk_2019/melk_2019_2.html')

def melk_2019_3(request):
  return render(request, 'tutorials_cctbx/melk_2019/melk_2019_3.html')

def melk_2019_4(request):
  return render(request, 'tutorials_cctbx/melk_2019/melk_2019_4.html')

def melk_2019_5(request):
  return render(request, 'tutorials_cctbx/melk_2019/melk_2019_5.html')

def melk_2019_intro(request):
  args = {'is_active': 'display: block;'}
  return render(request, 'tutorials_cctbx/melk_2019/melk_2019_intro.html', args)

def flex_array(request):
  args = {'is_active_doc': 'display: block;'}
  return render(request, 'tutorials_cctbx/flex_array/flex_array.html', args)

