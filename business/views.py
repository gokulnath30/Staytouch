from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from django_filters import rest_framework as filters
from .models import Business
from .permissions import IsOwnerOrReadOnly
from .serializers import BusinessSerializer
from .pagination import CustomPagination
from .filters import BusinessFilter


class CreateBusiness(ListCreateAPIView):
    serializer_class = BusinessSerializer
    queryset = Business.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = BusinessFilter

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


class UpdateBusiness(RetrieveUpdateDestroyAPIView):
    serializer_class = BusinessSerializer
    queryset = Business.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]





