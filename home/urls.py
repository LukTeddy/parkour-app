from django.urls import path
from django.conf import settings
from .views import PostListView
from . import views

urlpatterns = [
    path('', views.home, name='home-menu'),
    # path('adelaide/', views.adelaide, name='adelaide-menu'),
    path('spots/add', views.add_spot, name='add-spot'),
    path('spots/', views.spot_list, name='spot-list'),
    path('spots/<int:spot_id>/', views.spot_detail, name='spot-detail'),
    path('comments/<int:comment_id>/delete/', views.delete_comment, name='delete-comment')
]