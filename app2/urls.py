from django.urls import path
from . import views
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='vista1/')),
    path('vista1/', views.vista1, name='vista1'),
    path('vista2/', views.vista2, name='vista2'),
]