from django.views.generic import DateDetailView, ListView, TemplateView
from django.views.generic.base import ContextMixin

from .models import Article, Category


class CategoriesMixin(ContextMixin):
    def get_context_data(self, **kwargs: any) -> dict[str, any]:
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        return context


class HomePageView(CategoriesMixin, TemplateView):
    model = Article
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context["articles"] = Article.objects.filter(main_page=True)[:5]
        return context


class ArticleDetail(CategoriesMixin, DateDetailView):
    model = Article
    template_name = "article-detail.html"
    context_object_name = "item"
    date_field = "pub_date"
    query_pk_and_slug = True
    month_format = "%m"
    allow_future = True

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        try:
            context["images"] = context["item"].images.all()
        except Exception:
            pass

        return context


class ArticleList(CategoriesMixin, ListView):
    model = Article
    template_name = "articles-list.html"
    context_object_name = "items"

    def get_context_data(self, *args, **kwargs):
        context = super(ArticleList, self).get_context_data(*args, **kwargs)

        try:
            context["category"] = Category.objects.get(slug=self.kwargs.get("slug"))
        except Exception:
            context["category"] = None

        return context

    def get_queryset(self, *args, **kwargs):
        articles = Article.objects.all()
        return articles


class ArticleCategoryList(ArticleList):
    def get_queryset(self, *args, **kwargs):
        articles = Article.objects.filter(category__slug__in=[self.kwargs["slug"]]).distinct()
        return articles
