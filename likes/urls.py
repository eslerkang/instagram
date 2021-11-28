from django.urls import path

from likes.views import LikeView

urlpatterns = [
    path('', LikeView.as_view()),
]
