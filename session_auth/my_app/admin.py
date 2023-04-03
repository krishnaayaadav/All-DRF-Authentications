from django.contrib import admin

from .models import Article

# Register your models here.

@admin.register(Article)
class ArticleModel(admin.ModelAdmin):
   list_display  = ('id', 'title', 'description', 'author')