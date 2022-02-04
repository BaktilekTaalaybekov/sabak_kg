from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('category/<int:category_id>/', get_category, name='category'),
    path('lesson/<int:lesson_id>/', view_lesson, name='view_lesson'),
    path('lesson/add-lesson/', add_lesson, name='add_lesson'),
]
