from django.shortcuts import render

import datetime

from books.models import Book


def books_view(request, date = None):

    books = Book.objects.order_by('-pub_date')

    dates = set(book.pub_date for book in books)
    dates = sorted(list(dates))


    template = 'books/books_list.html'

    if date is None:
        context = {'books': books, 'dates': dates}

    else:
        print(dates)
        date = datetime.strptime(date, '%Y-%m-%d').date()
        books = Book.objects.filter(pub_date=date)
        date_index = dates.index(date)
        if date_index > 0:
            previos_date = dates[date_index - 1]
        else:
            previos_date = None

        if date_index < len(dates) - 1:
            next_date = dates[date_index + 1]
        else:
            next_date = None

        context = {'books': books,'previos_date': previos_date,'next_date': next_date}

    return render(request, template, context)
