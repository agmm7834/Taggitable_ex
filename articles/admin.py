from django.contrib import admin

from .models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    list_filter = ('created_at', 'tags')
    search_fields = ('title', 'content', 'tags__name')
    prepopulated_fields = {'slug': ('title',)}
