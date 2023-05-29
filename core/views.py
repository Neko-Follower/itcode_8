from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from core import models


# Create your views here.
class TitleMixin:
    title = None

    def get_title(self):
        return self.title

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = self.get_title()
        return context


class GroupList(TitleMixin, ListView):
    model = models.Group
    template_name = 'groups.html'
    context_object_name = 'groups'
    title = 'Группы'


class CourseList(TitleMixin, ListView):
    model = models.Course
    template_name = 'courses.html'
    context_object_name = 'courses'
    title = 'Курсы'


class UserList(TitleMixin, ListView):
    model = models.User
    template_name = 'users.html'
    context_object_name = 'users'
    title = 'Пользователи'


class UserDetail(TitleMixin, DetailView):
    model = models.User
    template_name = 'user_detail.html'
    context_object_name = 'user'
    title = 'Профиль пользователя'


def get_main_page(request):
    return render(request=request, template_name='main.html', context={'title': 'Главная'})