from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('event/create', views.EventCreate.as_view(), name='event-create'),
    path('event/<uuid:pk>/', views.EventDetail.as_view(), name='event-detail'),
    path('event/<uuid:pk>/update', views.EventUpdate.as_view(), name='event-update'),
    # path('event/<int:pk>/responses', views.EventDetailView.as_view(), name='event-detail')
]
