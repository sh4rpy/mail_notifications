from django.urls import path

from . import views


urlpatterns = [
    path('', views.NotificationListView.as_view(), name='list'),
    path('new/', views.CreateNotificationView.as_view(), name='new'),
    path('update/<int:pk>/', views.UpdateNotificationView.as_view(), name='update'),
    path('delete/<int:pk>/', views.DeleteNotificationView.as_view(), name='delete'),
]
