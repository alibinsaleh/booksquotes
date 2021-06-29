from django.urls import path
from main import views

urlpatterns = [
	path('', views.books_home),
	path('book/<book_id>', views.book_details)
]