from django.conf.urls import url
from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.index, name='index_phenix'),
    #
    path('installation/', views.installation, name='installation_phenix'),
    #
    path('overview/', views.overview, name='overview_phenix'),
    path('doc_quick_reference/', views.doc_quick_reference, name='doc_quick_reference_phenix'),
    path('directory_structure/', views.directory_structure, name='directory_structure_phenix'),
    #
    path('doc_mb_intro/', views.doc_mb_intro, name='doc_mb_intro_phenix'),
    path('doc_mb_read_files/', views.doc_mb_read_files, name='doc_mb_read_files_phenix'),
    path('doc_mb_fit_ligand/', views.doc_mb_fit_ligand, name='doc_mb_fit_ligand_phenix'),
    path('doc_mb_model_building/', views.doc_mb_model_building, name='doc_mb_model_building_phenix'),
    path('doc_mb_loop_fitting/', views.doc_mb_loop_fitting, name='doc_mb_loop_fitting_phenix'),
    path('doc_mb_replace_segment/', views.doc_mb_replace_segment, name='doc_mb_replace_segment_phenix'),
    path('doc_mb_morphing/', views.doc_mb_morphing, name='doc_mb_morphing_phenix'),
    path('doc_mb_sequence/', views.doc_mb_sequence, name='doc_mb_sequence_phenix'),
    #
    path('restraint_jiffys/', views.restraint_jiffys, name='restraint_jiffys_phenix'),
    #
    path('prog_program_template/', views.prog_program_template, name='prog_program_template_phenix'),
    path('prog_runsnake/', views.prog_runsnake, name='prog_runsnake_phenix'),
    path('prog_lineprofiler/', views.prog_lineprofiler, name='prog_lineprofiler_phenix'),
    path('prog_cplusplus_fast_compile/', views.prog_cplusplus_fast_compile, name='prog_cplusplus_fast_compile_phenix'),
    #
    path('template/', views.template, name='template_phenix'),
]
