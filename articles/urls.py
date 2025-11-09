from django.urls import path

from .views import (
    ArticleCreateView,
    ArticleDetailView,
    ArticleListView,
    TagDetailView,
)

app_name = 'articles'

urlpatterns = [
    path('', ArticleListView.as_view(), name='list'),
    path('write/', ArticleCreateView.as_view(), name='create'),
    path('tag/<slug:tag_slug>/', ArticleListView.as_view(), name='by_tag'),
    path('tags/<slug:slug>/', TagDetailView.as_view(), name='tag-detail'),
    path('<slug:slug>/', ArticleDetailView.as_view(), name='detail'),
]

