from django.urls import path

from comments.views import CommentView

urlpatterns = [
    path('', CommentView.as_view()),
]
