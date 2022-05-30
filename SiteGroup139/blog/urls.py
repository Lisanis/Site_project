from django.urls import path
from . import views

urlpatterns = [
    path('blog/', views.BlogListView.as_view(), name='blog'),
    path('post/<int:pk>/', views.BlogDetailView.as_view(), name='post_detail')
]
