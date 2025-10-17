from django.urls import path
from .views import course_list, course_detail

urlpatterns = [
    path('', course_list, name='courses_index'),
    path('<slug:slug>/', course_detail, name='course_detail'),
]


