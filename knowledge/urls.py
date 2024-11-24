from django.urls import include, path
from knowledge import views

urlpatterns = [
    path('title/', views.view_title),
    # path('knowledge/', 'knowledge.urls'),
]
