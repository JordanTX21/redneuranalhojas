from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from django_filters import rest_framework as filters
from .models import Hoja
from .permissions import IsOwnerOrReadOnly
from .serializers import HojaSerializer
from .pagination import CustomPagination
from .filters import HojaFilter


class ListCreateHojaAPIView(ListCreateAPIView):
    serializer_class = HojaSerializer
    queryset = Hoja.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = HojaFilter

    def perform_create(self, serializer):
        # Assign the user who created the Hoja
        serializer.save(creator=self.request.user)


class RetrieveUpdateDestroyHojaAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = HojaSerializer
    queryset = Hoja.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]





