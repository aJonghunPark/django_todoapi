from django.conf.urls import include
from django.urls import path
from rest_framework import routers

from api.views import CreateUserView, MyProfileView, TaskViewSet

router = routers.DefaultRouter()
# viewsets.ModelViewSetを継承したものはrouterに登録できる。
router.register("tasks", TaskViewSet, basename="tasks")

urlpatterns = [
    path("myself/", MyProfileView.as_view(), name="myself"),
    path("register/", CreateUserView.as_view(), name="register"),
    path("", include(router.urls)),
]
