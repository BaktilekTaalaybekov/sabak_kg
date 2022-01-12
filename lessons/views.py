from django.shortcuts import render
from .models import Lesson, Category


def index(request):
    lessons = Lesson.objects.all()
    categories = Category.objects.all()
    context = {
        'lessons_k': lessons,
        'title_k': 'LESSONS LIST',
        'categories_k': categories,
    }
    return render(request, 'lessons/index.html', context)


def get_category(request, category_id):
    lessons = Lesson.objects.filter(category_id=category_id)
    categories = Category.objects.all()
    category = Category.objects.get(pk=category_id)
    return render(request, 'lessons/category.html',
                  {'lessons_k_gk': lessons, 'categories_k_gk': categories, 'category_k_gk': category})
