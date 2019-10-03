from django.urls import path
from blog import views

urlpatterns = [
    path('',views.PostListView.as_view(),name = 'post_list'),
    path('about/',views.AboutView.as_view(),name = 'about'),
    path('post/<int:pk>',views.PostDetailView.as_view(),name='post_detail'),
    path('post/new/',views.PostCreateView.as_view(),name = 'post_new'),
    path('post/<int:pk>/edit/',views.PostUpdateView.as_view(),name='post_edit'),
    path('post/<int:pk>/remove/',views.PostDeleteView.as_view(),name='post_remove'),
    path('draft/',views.DraftListView.as_view(),name = 'draft_list'),
    path('post/<int:pk>/comment/',views.add_comment_to_post,name='add_comment_to_post'),
    path('comment/<int:pk>/approve/',views.approve_comment,name='comment_approve'),
    path('comment/<int:pk>/remove/',views.delete_comment,name='comment_remove'),
    path('post/<int:pk>/publish/',views.post_publish,name='post_publish'),

]
