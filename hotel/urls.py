from django.urls import path 
from . import views
from .views import reservation_view
from django.views.generic import TemplateView

urlpatterns = [
    path('',views.index, name='index' ),
    path('reservation/', reservation_view, name='reservation'),
    path('thank_you/', TemplateView.as_view(template_name='hotel/thank_you.html'), name='thank_you'),


]