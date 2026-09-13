from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='app1/index.html')),
    path('vista1/', views.vista1, name='vista1'),
    path('vista2/', views.vista2, name='vista2'),
]