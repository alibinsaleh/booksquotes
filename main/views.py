from django.shortcuts import render

# Create your views here.

def retrieve_books_data():
	with open('books.dat', 'r') as file:
		books = file.readlines()

	mybooks = []	
	for book in books:
		current_book = book.split(',')
		mybooks.append(current_book)

	return mybooks

def books_home(request):
	mybooks = retrieve_books_data()	
	return render(request, 'books/index.html', context={'mybooks': mybooks})

def book_details(request, book_id):
	mybooks = retrieve_books_data()
	for book in mybooks:
		if str(book[0]) == str(book_id):
			mybook = book
			break


	return render(request, 'books/book_details.html', context={'mybook': mybook})