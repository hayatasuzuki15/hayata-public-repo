from django.shortcuts import render

from django.views.generic import TemplateView, ListView, DetailView,DeleteView,CreateView
from .models import BlogModel

class Menu(TemplateView):
    template_name = "menu.html"
    print("追加")

class BlogList(ListView):
    template_name = "list.html"
    context_object_name = "items"
    model = BlogModel

class BlogDetail(DetailView):
    template_name = "detail.html"
    context_object_name = "item"
    model = BlogModel


class BlogCreate(CreateView):
    model = BlogModel
    template_name = "create.html"
