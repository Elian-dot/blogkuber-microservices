from django.urls import path

from .views import *

urlpatterns = [
    path('get/profile/<id>', GetUserProfileView.as_view()),
]