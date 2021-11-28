from django.urls import path

from users.views import SignupView, SigninView, FollowView

urlpatterns = [
    path('/signup', SignupView.as_view()),
    path('/signin', SigninView.as_view()),
    path('/follow', FollowView.as_view()),
]
