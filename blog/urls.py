from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('register/', views.UserRegistrationView.as_view(), name='registration'),
    path('login/', views.MyLoginView.as_view(), name='login'),
    path('logout/', views.MyLogoutView.as_view(), name='logout'),
    path('', views.PostFeedView.as_view(), name='feed'),
    path('createpost', views.CreatePostView.as_view(), name='create-post'),
    path('updatepost/<int:pk>', views.UpdatePostView.as_view(), name='update-post'),
    path('comment/<int:pk>', views.CreateCommentView.as_view(), name='create-comment'),
    path('post/delete/<int:pk>', views.DeletePostView.as_view(), name='delete-post')
]