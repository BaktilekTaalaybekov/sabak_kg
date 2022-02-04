from django import forms
from .models import Lesson


# class LessonForm(forms.Form):
    # title = forms.CharField(max_length=150, label='Название', widget=forms.TextInput(attrs={"class": "form-control"}))
    # video = forms.FileField(label='Видео', widget=forms.FileInput(attrs={"class": "form-control"}))
    # description = forms.CharField(label='Описание', widget=forms.Textarea(attrs={"class": "form-control"}))
    # home_work = forms.URLField(label='Домашнее задание', widget=forms.TextInput(attrs={"class": "form-control"}))
    # is_published = forms.BooleanField(label='Опубликовано', initial=True)
    # category = forms.ModelChoiceField(queryset=Category.objects.all(), label='Категория',
    #                                   empty_label='Выберите категорию', widget=forms.Select(attrs={"class": "form-control"}))

class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ['title', 'video', 'description', 'home_work', 'is_published', 'category']
        widgets = {
            'title': forms.TextInput(attrs={"class": "form-control"}),
            'video': forms.FileInput(attrs={"class": "form-control"}),
            'description': forms.Textarea(attrs={"class": "form-control"}),
            'home_work': forms.TextInput(attrs={"class": "form-control"}),
            'category': forms.Select(attrs={"class": "form-control"}),
        }
