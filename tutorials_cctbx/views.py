from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
  return render(request, 'tutorials_cctbx/index.html')
  #return HttpResponse("Hello, world. You're at the polls index.")

def melk_2019_1(request):
  return render(request, 'tutorials_cctbx/melk_2019/melk_2019_1.html')

def melk_2019_2(request):
  return render(request, 'tutorials_cctbx/melk_2019/melk_2019_2.html')

def melk_2019_3(request):
  return render(request, 'tutorials_cctbx/melk_2019/melk_2019_3.html')

def melk_2019_4(request):
  return render(request, 'tutorials_cctbx/melk_2019/melk_2019_4.html')

def melk_2019_5(request):
  return render(request, 'tutorials_cctbx/melk_2019/melk_2019_5.html')

def melk_2019_intro(request):
  return render(request, 'tutorials_cctbx/melk_2019/melk_2019_intro.html')
