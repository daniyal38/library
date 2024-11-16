from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from django.utils import timezone
from datetime import timedelta
from rest_framework.permissions import IsAdminUser

# Create your views here.
class BookListView(generics.ListAPIView):
    serializer_class = BookSerializer
    
    def get_queryset(self):
        queryset = Book.objects.all()
        author = self.request.query_params.get('author')
        published_date = self.request.query_params.get('published_date')

        if author:
            queryset = queryset.filter(author__icontains=author)

        if published_date:
            queryset = queryset.filter(published_date=published_date)
        
        return queryset


        
    
class BookRetrieveView(generics.RetrieveAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    lookup_field = 'id'


class BookCreateView(generics.CreateAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    permission_classes = []
    

class BookUpdateView(generics.UpdateAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    
    lookup_field = 'id'


class BookRecentView(generics.ListAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        
        thirty_days_ago = timezone.now().date() - timedelta(days=30)

        return Book.objects.filter(published_date__gte = thirty_days_ago, is_deleted=False)
    

class BookDeleteView(generics.DestroyAPIView):
    permission_classes = [IsAdminUser]
    queryset = Book.objects.all()

    def perform_destroy(self, instance):
        instance.is_deleted = True
        instance.save()

    


    