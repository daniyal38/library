from django.urls import path
from .views import BookListView, BookRetrieveView,BookCreateView,BookUpdateView,BookRecentView, BookDeleteView


urlpatterns = [
    path('<int:id>/', BookRetrieveView.as_view(), name='book-detail'),
    path('', BookListView.as_view(), name='book-list'),
    path('create/', BookCreateView.as_view(), name='book-create'),
    path('update/<int:id>', BookUpdateView.as_view(), name='book-update'),
    path('delete/<int:id>', BookDeleteView.as_view(), name='book-delete'),
    path('recent/', BookRecentView.as_view(), name='recent-books'),

]
