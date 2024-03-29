from django.urls import path, re_path, register_converter
from . import views
from . import converter

register_converter(converter.FourDigitalYearConverter, "year4")

urlpatterns = [
	path('', views.index),
	path('cat/<int:cat_id>/', views.categories),
	path('cat/<slug:cat_slug>/', views.categories_by_slug),
	path('archive/<year4:year>/', views.archive)
]