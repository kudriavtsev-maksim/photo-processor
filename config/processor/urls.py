from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('upload/', views.upload_image, name='upload_image'),
    path('upload-multiple/', views.upload_multiple_images, name='upload_multiple'),   
]

