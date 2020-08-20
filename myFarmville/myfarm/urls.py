from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, FilterView
from . import views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', PostListView.as_view(), name='myfarm-home'),
    path('post/<int:pk>', PostDetailView.as_view(), name='myfarm-detail'),
    path('post/new/', PostCreateView.as_view(), name='myfarm-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='myfarm-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='myfarm-delete'),
    path('about/', views.about, name='myfarm-about'),
    path('filter/', FilterView.as_view(), name='myfarm-filter'),
    path('categories/', views.categories, name='myfarm-categories'),
    path('vegetable/', views.vegetable, name='myfarm-vegetable'),
    path('fruits/', views.fruits, name='myfarm-fruits'),
]
#<app>/<model>_<viewtype>.html

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)