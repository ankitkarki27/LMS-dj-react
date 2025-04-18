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
    path('teachers/<int:pk>/',views.TeacherList.as_view()),
    path('teachers/<int:pk>/update/',views.TeacherList.as_view()),
    path('teachers/<int:pk>/delete/',views.TeacherList.as_view()),
    
    # path('courses/',views.CourseList.as_view()),
    
]
