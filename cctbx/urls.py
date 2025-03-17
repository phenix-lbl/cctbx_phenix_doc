from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('installation/', views.installation, name='installation'),

    path('getting_started/', views.getting_started, name='getting_started'),

    path('documentation_overview/', views.documentation_overview, name='documentation_overview'),

    path('doc_programming_tips_1/', views.doc_programming_tips_1, name='doc_programming_tips_1'),
    path('doc_programming_tips_2/', views.doc_programming_tips_2, name='doc_programming_tips_2'),
    path('doc_programming_tips_3/', views.doc_programming_tips_3, name='doc_programming_tips_3'),
    path('doc_programming_tips_4/', views.doc_programming_tips_4, name='doc_programming_tips_4'),


    path('doc_hklviewer/', views.doc_hklviewer, name='doc_hklviewer'),

    path('doc_hlo_intro/', views.doc_hlo_intro, name='doc_hlo_intro'),
    path('doc_hlo_data_manager/', views.doc_hlo_data_manager, name='doc_hlo_data_manager'),
    path('doc_hlo_model_manager/', views.doc_hlo_model_manager, name='doc_hlo_model_manager'),
    path('doc_hlo_map_manager/', views.doc_hlo_map_manager, name='doc_hlo_map_manager'),
    path('doc_hlo_model_map_manager/', views.doc_hlo_model_map_manager, name='doc_hlo_model_map_manager'),

    path('doc_maps_intro/', views.doc_maps_intro, name='doc_maps_intro'),
    path('doc_maps_boxing/', views.doc_maps_boxing, name='doc_maps_boxing'),

    path('doc_low_flex_array/', views.doc_low_flex_array, name='doc_low_flex_array'),
    path('doc_low_flex_advanced/', views.doc_low_flex_advanced, name='doc_low_flex_advanced'),
    path('doc_low_phil/', views.doc_low_phil, name='doc_low_phil'),
    path('doc_low_array_family/', views.doc_low_array_family, name='doc_low_array_family'),
    path('doc_low_scitbx_tour/', views.doc_low_scitbx_tour, name='doc_low_scitbx_tour'),

    path('doc_models_hierarchy/', views.doc_models_hierarchy, name='doc_models_hierarchy'),

    path('tuto_intro/', views.tuto_intro, name='tuto_intro'),
    path('tuto_hklviewer/', views.tuto_hklviewer, name='tuto_hklviewer'),
    path('tuto_melk_2019/', views.tuto_melk_2019, name='tuto_melk_2019'),
    path('tuto_rigid_body/', views.tuto_rigid_body, name='tuto_rigid_body'),
    path('tuto_cctbx_tour/', views.tuto_cctbx_tour, name='tuto_cctbx_tour'),

    path('script_toc/', views.script_toc, name='script_toc'),
    path('script_1/', views.script_1, name='script_1'),
    path('script_compare_ss/', views.script_compare_ss, name='script_compare_ss'),
    path('script_ideal_ss/', views.script_ideal_ss, name='script_ideal_ss'),
    path('script_lbfgs_no_curvature/', views.script_lbfgs_no_curvature, name='script_lbfgs_no_curvature'),
    path('script_lbfgs_with_curvature/', views.script_lbfgs_with_curvature, name='script_lbfgs_with_curvature'),
    path('script_rfactors/', views.script_rfactors, name='script_rfactors'),
    #
    path('newsletter_artcls/', views.newsletter_artcls, name='newsletter_artcls'),

    path('about/', views.about, name='about'),

    path('test/', views.test, name='test'),
]
