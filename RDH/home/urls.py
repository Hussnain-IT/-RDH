from django.urls import path
from . import views

urlpatterns = [
    path('add-property/', views.add_property, name='add_property'),
    path('', views.home_view, name='home'),
    path('properties/', views.properties_view, name='properties'),
    path('properties/type/<str:property_type>/', views.property_type_view, name='property_type'),
    path('5-marla/', views.marla_5_view, name='5-marla'),
    path('7-marla/', views.marla_7_view, name='7-marla'),
    path('10-marla/', views.marla_10_view, name='10-marla'),
    path('1-kanal/', views.kanal_view, name='1-kanal'),
    path('terms/', views.terms_view, name='terms'),
    path('contact/', views.contact_view, name='contact'),
    path('C.A/', views.CA_view, name='C.A'),
    path('C.A/proUI.html', views.CA_proUI_view, name='CA_proUI'),
    path('property/<int:pk>/update-status/', views.update_property_status, name='update_property_status'),
    path('property/<int:pk>/delete/', views.delete_property, name='delete_property'),
    path('property-search/', views.property_search_view, name='property_search'),
    path('property/<int:pk>/', views.property_detail_view, name='property_detail'),
]
