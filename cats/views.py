from rest_framework import viewsets
from .serializer import CatSerializer
from .models import Cats

#* Create CRUD.
class CatsView(viewsets.ModelViewSet):
    serializer_class = CatSerializer
    queryset = Cats.objects.all()