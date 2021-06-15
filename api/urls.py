from django.urls import path
from . views import PostList, PostDetail

app_name = "api"

urlpatterns = [
    path("<int:pk>/", PostDetail.as_view(), name="post-details"),
    path("", PostList.as_view(), name="post-list"),
]
