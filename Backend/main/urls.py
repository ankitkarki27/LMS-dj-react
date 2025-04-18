from django.urls import path, include
from . import models
from django.contrib import admin
from .views import TeacherList
from rest_framework import routers
# from rest_framework.authtoken.views import ObtainAuthToken
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('teachers/',views.TeacherList.as_view()),
    path('teachers/<int:pk>/',views.TeacherDetail.as_view()),
    
    path('courses/<int:pk>/',views.CourseDetail.as_view()),
    path('courses/',views.CourseList.as_view()),
    
    
    
    
    # path('courses/',views.CourseList.as_view()),
    
]
