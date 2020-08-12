from django.urls import path, re_path, include
from django.conf.urls import url
from .views import (
    BlogListView, 
    PostDeleteView, 
    PostUpdateView, 
    PostDetailView, 
    PostCreateView, 
    ProfileView, 
    CommentCreateView, 
    ProfileUpdateView, 
    CommentDeleteView,
    NotificationView)

import notifications.urls

urlpatterns = [
    path('', BlogListView.as_view(), name = 'home'),
    path('<int:pk>/edit/', PostUpdateView.as_view(), name='post_edit'),
    path('<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('<int:pk>/detail/', PostDetailView.as_view(), name='post_detail'),
    path('newpost/', PostCreateView.as_view(), name='post_create'),
    path('<int:pk>/comment/', CommentCreateView.as_view(), name='comment'),
    path('<int:pk>/profile/', ProfileView.as_view(), name='profile'),
    path('<int:pk>/profileupdate/', ProfileUpdateView.as_view(), name='profileupdate'),
    path('<int:pk>/comment_delete/', CommentDeleteView.as_view(), name='comment_delete'),
    path('notification/', NotificationView.as_view(), name='notification'),
    url('^inbox/notifications/', include(notifications.urls, namespace='notifications')),
    #path('<int:pk>/profile/', index_page, name='profile'),
    #re_path(r'^user/(?P<author>\w+)/$', ProfileView.as_view(), name='profile'),
]