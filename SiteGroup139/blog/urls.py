from django.urls import path
from . import views

urlpatterns = [
    path('blog/', views.BlogListView.as_view(), name='blog'),
    path('blog/post/<int:pk>/', views.BlogDetailView.as_view(), name='post_detail'),
    path('blog/post/new/', views.BlogCreateView.as_view(), name='post_new'),
    path('blog/post/<int:pk>/edit/', views.BlogUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete/', views.BlogDeleteView.as_view(), name='post_delete'),
    path('credits/', views.Credentials.as_view(), name='credits'),
]
