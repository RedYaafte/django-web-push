from django.urls import path
from .views import WebPushView, onesignal_register

urlpatterns = [
    path('', WebPushView.as_view(), name='index'),
    path('onesignal-register/', onesignal_register, name='onesignal_register'),
]
