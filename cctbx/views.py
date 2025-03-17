from django.shortcuts import render
from django.http import HttpResponse


def index(request):
  return render(request, 'cctbx/index.html')
  #return HttpResponse("Hello, world. You're at the polls index.")

# ------------------------------------------------------------------------------

def installation(request):
  return render(request, 'cctbx/installation.html')

# ------------------------------------------------------------------------------

def getting_started(request):
  return render(request, 'cctbx/documentation/getting_started.html')

# ------------------------------------------------------------------------------

def documentation_overview(request):
  return render(request, 'cctbx/documentation/documentation_overview.html')

# ------------------------------------------------------------------------------

def doc_programming_tips_1(request):
  return render(request, 'cctbx/documentation/website_html/doc_programming_tips_1.html')

# ------------------------------------------------------------------------------

def doc_programming_tips_2(request):
  return render(request, 'cctbx/documentation/website_html/doc_programming_tips_2.html')

# ------------------------------------------------------------------------------

def doc_programming_tips_3(request):
  return render(request, 'cctbx/documentation/website_html/doc_programming_tips_3.html')

# ------------------------------------------------------------------------------

def doc_programming_tips_4(request):
  return render(request, 'cctbx/documentation/doc_programming_tips_4.html')

# ------------------------------------------------------------------------------

def doc_hklviewer(request):
  return render(request, 'cctbx/documentation/doc_hklviewer.html')

# ------------------------------------------------------------------------------
# subsubmenu1
def doc_low_phil(request):
  return render(request, 'cctbx/documentation/doc_low_phil.html')

def doc_hlo_intro(request):
  return render(request, 'cctbx/documentation/website_html/doc_hlo_intro.html')

def doc_hlo_data_manager(request):
  return render(request, 'cctbx/documentation/website_html/doc_hlo_data_manager.html')

def doc_hlo_model_manager(request):
  return render(request, 'cctbx/documentation/website_html/doc_hlo_model_manager.html')

def doc_hlo_map_manager(request):
  return render(request, 'cctbx/documentation/website_html/doc_hlo_map_manager.html')

def doc_hlo_model_map_manager(request):
  return render(request, 'cctbx/documentation/website_html/doc_hlo_model_map_manager.html')

# ------------------------------------------------------------------------------
#   subsubmenu2
def doc_low_flex_array(request):
  return render(request, 'cctbx/documentation/doc_low_flex_array.html')

def doc_low_flex_advanced(request):
  return render(request, 'cctbx/documentation/website_html/doc_low_flex_advanced.html')

def doc_low_array_family(request):
  return render(request, 'cctbx/documentation/doc_low_array_family.html')

def doc_low_scitbx_tour(request):
  return render(request, 'cctbx/documentation/doc_low_scitbx_tour.html')

# ------------------------------------------------------------------------------
#   subsubmenu3
def doc_maps_intro(request):
  return render(request, 'cctbx/documentation/website_html/doc_maps_intro.html')

def doc_maps_boxing(request):
  return render(request, 'cctbx/documentation/website_html/doc_maps_boxing.html')

# ------------------------------------------------------------------------------

#   subsubmenu4
def doc_models_hierarchy(request):
  return render(request, 'cctbx/documentation/website_html/doc_models_hierarchy.html')

# ------------------------------------------------------------------------------

def tuto_intro(request):
  return render(request, 'cctbx/tutorials/tuto_intro.html')

def tuto_hklviewer(request):
  return render(request, 'cctbx/tutorials/tuto_hklviewer.html')

def tuto_melk_2019(request):
  return render(request, 'cctbx/tutorials/tuto_melk_2019.html')

def tuto_rigid_body(request):
  return render(request, 'cctbx/tutorials/tuto_rigid_body.html')

def tuto_cctbx_tour(request):
  return render(request, 'cctbx/tutorials/tuto_cctbx_tour.html')

# ------------------------------------------------------------------------------

def script_toc(request):
  return render(request, 'cctbx/script_toc.html')

def script_1(request):
  return render(request, 'cctbx/documentation/website_html/script_1.html')

def script_compare_ss(request):
  return render(request, 'cctbx/documentation/website_html/script_compare_ss.html')

def script_ideal_ss(request):
  return render(request, 'cctbx/documentation/website_html/script_ideal_ss.html')

def script_lbfgs_no_curvature(request):
  return render(request, 'cctbx/documentation/website_html/script_lbfgs_no_curvature.html')

def script_lbfgs_with_curvature(request):
  return render(request, 'cctbx/documentation/website_html/script_lbfgs_with_curvature.html')

def script_rfactors(request):
  return render(request, 'cctbx/documentation/website_html/script_rfactors.html')

# ------------------------------------------------------------------------------

def newsletter_artcls(request):
  return render(request, 'cctbx/newsletter_artcls.html')

# ------------------------------------------------------------------------------

def about(request):
  return render(request, 'cctbx/about.html')

# ------------------------------------------------------------------------------

def test(request):
  return render(request, 'cctbx/test.html')

