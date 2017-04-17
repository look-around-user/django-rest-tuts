from rest_framework import mixins
from rest_framework import generics
from .models import Snippet
from .serializers import SnippetSerializer


class SnippetList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def get(self, request, *args, **kwargs):
        return self.list(self, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(self, *args, **kwargs)


class SnippetDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(self, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(self, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(self, *args, **kwargs)
