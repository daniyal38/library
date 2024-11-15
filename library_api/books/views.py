from rest_framework import generics, permissions
from rest_framework.response import Response
from django.utils import timezone
from datetime import timedelta

from .models import Book
from .serializers import BookSerializer

class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.filter(is_deleted=False)
    serializer_class = BookSerializer
    lookup_field = 'id'

class BookListView(generics.ListAPIView):
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        queryset = Book.objects.filter(is_deleted=False)
        author = self.request.query_params.get('author')
        published_date = self.request.query_params.get('published_date')
        if author:
            queryset = queryset.filter(author__icontains=author)
        if published_date:
            queryset = queryset.filter(published_date=published_date)
        return queryset

class CreateBookView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAdminUser]

class UpdateBookView(generics.UpdateAPIView):
    queryset = Book.objects.filter(is_deleted=False)
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAdminUser]
    lookup_field = 'id'

class DeleteBookView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    permission_classes = [permissions.IsAdminUser]

    def perform_destroy(self, instance):
        instance.is_deleted = True
        instance.save()

class RecentBooksView(generics.ListAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        thirty_days_ago = timezone.now().date() - timedelta(days=30)
        return Book.objects.filter(published_date__gte=thirty_days_ago, is_deleted=False)