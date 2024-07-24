from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index, name='Index'),
    path('Contact', views.Contact, name='Contact'),
    path('About', views.About, name='About'),
    path('Deworming', views.Deworming, name='Deworming'),
    path('Rollback', views.Rollback, name='Rollback'),
]
