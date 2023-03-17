from django.urls import path

from . import views

app_name = 'riddles'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('blog/', views.blog, name='blog'),
    path('about/', views.about, name='about'),
    path('blog-details/', views.blog_details, name='blog-details'),
    # path('checkout/', views.checkout, name='checkout'),
    path('results/', views.results, name='results'),
    path('shop/', views.shop, name='shop'),
    path('shop-details/', views.shop_details, name='shop-details'),
    path('shopping-cart/', views.shopping_cart, name='shopping-cart'),
    path('stats/', views.stats, name='stats'),
    path('contact/', views.contact, name='contact'),
]