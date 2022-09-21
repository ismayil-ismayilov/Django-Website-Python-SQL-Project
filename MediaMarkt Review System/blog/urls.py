from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='review-home'),
    path('average/', views.average, name='review-average'),
    path('list', views.PersonListView.as_view(), name='person_changelist'),
    path('add/', views.PersonCreateView.as_view(), name='person_add'),
    path('<int:pk>/', views.PersonUpdateView.as_view(), name='person_change'),
    path('review/', views.review, name='review'),
    path('ajax/load-cities/', views.load_cities, name='ajax_load_cities'),
    path('ajax/load-stores/', views.load_stores, name='ajax_load_stores'),
]

#    path('add/', views.PersonCreateView.as_view(), name='person_add'),