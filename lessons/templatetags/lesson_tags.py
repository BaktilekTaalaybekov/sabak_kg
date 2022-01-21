from django import template

from lessons.models import Category

register = template.Library()


@register.simple_tag(name='get_list_categories')
def get_categories():
    return Category.objects.all()


@register.inclusion_tag('lessons/list_categories.html')
def show_categories():
    categories = Category.objects.all()
    return {"categories_k": categories}
