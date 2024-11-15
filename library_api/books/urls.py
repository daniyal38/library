from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import path
from .views import BookDetailView, BookListView, CreateBookView, UpdateBookView, DeleteBookView, RecentBooksView

urlpatterns = [
    path('books/<int:id>/', BookDetailView.as_view(), name='book-detail'),
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/create/', CreateBookView.as_view(), name='book-create'),
    path('books/<int:id>/update/', UpdateBookView.as_view(), name='book-update'),
    path('books/<int:id>/delete/', DeleteBookView.as_view(), name='book-delete'),
    path('books/recent/', RecentBooksView.as_view(), name='recent-books'),
    path('auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]
