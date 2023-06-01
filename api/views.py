from rest_framework import generics, viewsets
from rest_framework.permissions import AllowAny

from .models import Task
from .serializers import TaskSerializer, UserSerializer


class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer
    # 新規でユーザーを生成するので、誰でもアクセスできるようにする。（アカウントが存在しない状態なので必要）
    permission_classes = (AllowAny,)


class MyProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer

    # ログインしているユーザー情報を返す。
    def get_object(self):
        return self.request.user


class TaskViewSet(viewsets.ModelViewSet):
    # querysetにTask.objects.all()することでTaskに関わるCRUD操作を行える。
    queryset = Task.objects.order_by("id").reverse()
    serializer_class = TaskSerializer
