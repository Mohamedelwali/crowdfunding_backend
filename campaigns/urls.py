from django.urls import path
from .views import *

urlpatterns = [
    path('', list_all_projects ),
    path('create/', create_project),
    path('<int:pk>/', get_project ),
    path('<int:pk>/update/', update_campaign ),
    path('<int:pk>/delete/', delete_project ),
    path('search/', search_campaigns),
]
