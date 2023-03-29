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
    path('shop/', views.ShopView.as_view(), name='shop'),
    path('shop-details/', views.shop_details, name='shop-details'),
    path('shopping-cart/', views.shopping_cart, name='shopping-cart'),
    path('stats/', views.stats, name='stats'),
    path('contact/', views.contact, name='contact'),
    path('virtual_try_on/', views.virtual_try_on, name='virtual_try_on'),
    path('virtual_try_on/result', views.virtual_try_on_result, name='virtual_try_on_result'),

    path('answer/', views.answer5, name='answer5'),
    path('answer0/', views.answer0, name='answer0'),
    path('answer1/', views.answer1, name='answer1'),
    path('answer2/', views.answer2, name='answer2'),
    path('answer3/', views.answer3, name='answer3'),
    path('answer4/', views.answer4, name='answer4'),

    path('questionaire/', views.questionaire, name='questionaire'),
    path('questionaire1/', views.questionaire1, name='questionaire1'),
    path('questionaire2/', views.questionaire2, name='questionaire2'),
    path('questionaire3/', views.questionaire3, name='questionaire3'),
    path('questionaire4/', views.questionaire4, name='questionaire4'),
    path('questionaire5/', views.questionaire5, name='questionaire5'),
]