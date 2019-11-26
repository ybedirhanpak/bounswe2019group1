from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^createnotification/', views.CreateNotificationAPIView.as_view(), name="create"),
    url(r'^listnotification/', views.ListNotificationAPIView.as_view(), name="create"),
]