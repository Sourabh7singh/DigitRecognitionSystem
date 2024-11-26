from django.urls import path
from .views import *
urlpatterns = [
    path('',HomeView.as_view(),name='index'),
    path('submit-image/',SubmitImageForRecognition.as_view(),name='submit-image'),
]
