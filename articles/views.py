from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView
from taggit.models import Tag

from .forms import ArticleForm
from .models import Article


class ArticleListView(ListView):
    model = Article
    template_name = 'articles/article_list.html'
    context_object_name = 'articles'
    paginate_by = 10

    def get_queryset(self):
        queryset = (
            super()
            .get_queryset()
            .select_related()
            .prefetch_related('tags')
        )
        tag_slug = self.kwargs.get('tag_slug')
        if tag_slug:
            queryset = queryset.filter(tags__slug=tag_slug)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tag_slug = self.kwargs.get('tag_slug')
        context['active_tag'] = None
        if tag_slug:
            context['active_tag'] = get_object_or_404(Tag, slug=tag_slug)
        context['tags'] = Tag.objects.all()
        return context


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'articles/article_detail.html'
    context_object_name = 'article'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'


class ArticleCreateView(CreateView):
    model = Article
    template_name = 'articles/article_form.html'
    form_class = ArticleForm
    success_url = reverse_lazy('articles:list')

    def form_valid(self, form):
        response = super().form_valid(form)
        form.save_m2m()
        return response


class TagDetailView(ListView):
    model = Article
    template_name = 'articles/tag_detail.html'
    context_object_name = 'articles'

    def get_queryset(self):
        self.tag = get_object_or_404(Tag, slug=self.kwargs['slug'])
        return (
            Article.objects.filter(tags__in=[self.tag])
            .distinct()
            .prefetch_related('tags')
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tag'] = self.tag
        context['tags'] = Tag.objects.all()
        return context
