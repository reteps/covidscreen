from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('event/<int:pk>/details', views.EventDetailView.as_view(), name='event-detail')
    # path('event/<int:pk>/responses', views.EventDetailView.as_view(), name='event-detail')
]
