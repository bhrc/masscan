from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('add-content/', views.add_content, name='add_content'),
    path('add-author/', views.ajax_add_author, name='add-author'),
    path('add-caty/', views.ajax_add_cat, name='add-cat'),
    path('add-tag/', views.ajax_add_tag, name='add-tag'),
    path('add-geotag/', views.ajax_add_geotag, name='add-geotag'),
    path('add-publication/', views.ajax_add_publication, name='add-publication'),
    path('contents/<int:id>', views.show_content, name='show_content'),
    path('contents/<int:id>/edit', views.update_content, name='update_content'),
    path("contents/<int:id>/delete", views.del_content, name="del_case"),
    path('contents/<slug:slug>', views.show_type, name='show_type'),
    path('<slug:slug>/<int:id>', views.show_cat, name='show_cat'),
]
