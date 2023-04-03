from django.urls import path
from .views import ArticleAPIView

urlpatterns = [
   path('article-api/', ArticleAPIView.as_view(), name='article_api'),
]
