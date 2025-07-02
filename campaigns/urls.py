from django.urls import path
from .views import campaign_search

urlpatterns = [
    path('projects/search/', campaign_search, name='project-search'),
]