from django.urls import path
from product import  views


urlpatterns = [
    path('addprod',views.addp,name='addprod'),
    path('<int:product_id>',views.detail,name='detail'),
    path('upvote/',views.upvote,name='upvote'),
    path('<int:product_id>/upvote/', views.upvote, name='upvote'),
    path('<int:product_id>/upvote', views.home, name='upvotehome'),
    path('ajax/', views.ajax, name='ajax'),
]
