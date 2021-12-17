from django.urls import path
from . import views
urlpatterns = [
    # path('$/', views.posts, name='posts'),
    # path('$/', views.comments, name='comments'),
    path('', views.profitpage, name='profitpage')
]