from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path("index/", TemplateView.as_view(template_name="blog/index.html")),
    path("", views.clubs, name="clubs"),
]
