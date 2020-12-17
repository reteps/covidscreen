from django.urls import path
from . import views

urlpatterns = [
    path('', views.UserEventList.as_view(), name='home'),
    path('all-events', views.AllEventList.as_view(), name='event-list-all'),
    path('my-events', views.UserEventList.as_view(), name='event-list'),
    path('event/create', views.EventCreate.as_view(), name='event-create'),
    path('event/join', views.join_event, name='event-join'),
    path('event/<uuid:pk>/', views.EventDetail.as_view(), name='event-detail'),
    path('event/<uuid:event>/responses', views.EventResponseList.as_view(), name='response-list'),
    path('event/<uuid:pk>/update', views.EventUpdate.as_view(), name='event-update'),
    # path('event/<uuid:event>/response/create', views.create_response, name='response-create'),
    path('event/<uuid:event>/response/create', views.ResponseCreateView.as_view(), name='response-create'),
    path('response/<int:pk>/', views.ResponseDetail.as_view(), name='response-detail'),
    path('response/<int:pk>/update', views.ResponseUpdate.as_view(), name='response-update'),
    # path('event/<int:pk>/responses', views.EventDetailView.as_view(), name='event-detail')
]
