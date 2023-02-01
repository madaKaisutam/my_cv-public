from django.urls import path
from my_cv_main_app import views as my_cv_main_app_view

app_name='main'
urlpatterns = [
    path('',my_cv_main_app_view.home),
    path('test',my_cv_main_app_view.home2, name='test'),
]