from django.urls import path

from .views import PostListAPIView, PostDetailAPIView, UserPostAPIView, UpvoteAPIView, CommentAPIView

urlpatterns = [
    path('posts', PostListAPIView.as_view()),
    path('posts/<int:pk>/', PostDetailAPIView.as_view()),
    path('posts/<int:pk>/upvote/', UpvoteAPIView.as_view()),
    path('posts/<int:pk>/comment/', CommentAPIView.as_view()),
    path('posts/<username>/', UserPostAPIView.as_view())
]
