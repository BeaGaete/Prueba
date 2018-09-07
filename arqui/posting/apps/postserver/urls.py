from django.urls import path

from apps.postserver.views import index

urlpatterns = [
    path('', index),
]