from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='myfarm-home'),
    path('post/<int:pk>', PostDetailView.as_view(), name='myfarm-detail'),
    path('post/new/', PostCreateView.as_view(), name='myfarm-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='myfarm-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='myfarm-delete'),
    path('about/', views.about, name='myfarm-about'),
    path('categories/', views.categories, name='myfarm-categories'),
]
#<app>/<model>_<viewtype>.html