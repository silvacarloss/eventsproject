from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:event_id>/', views.event_detail, name='details'),
    path('new', views.new_event, name='new'),
    path('save', views.save, name='save'),
]