from django.test import TestCase
from django.urls import resolve, reverse

from . import views


class HomeTests(TestCase):
    def test_home_view_status_code(self):
        url = reverse("home")
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        view = resolve("/")
        self.assertEquals(view.func.view_class, views.HomePageView)

    def test_category_view_status_code(self):
        url = reverse("articles-category-list", args=("name",))
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_category_url_resolves_category_view(self):
        view = resolve("/articles/category/name")
        self.assertEquals(view.func.view_class, views.ArticleCategoryList)

    def test_articles(self):
        url = reverse("articles-list")
        self.assertEquals(resolve(url).func.view_class, views.ArticleList)

    def test_article_detail(self):
        url = reverse(
            "article-detail",
            args=("2023", "09", "07", "5g-connectivity"),
        )
        self.assertEquals(resolve(url).func.view_class, views.ArticleDetail)
