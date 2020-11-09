import logging

from app import books

logger = logging.getLogger('scraping.menu')

USER_CHOICE = '''Enter one of the following
- 'b' to look at 5-star books
- 'c' to look at the cheapest books
- 'n' to just get the nect available book on the catalouge
- 'q' to quit

Enter your choice: '''

def print_best_books():
    logger.info('Finding best books by rating')
    best_books = sorted(books, key=lambda x: x.rating * -1)[:10]
    print('---Best Books---')
    for book in best_books:
        print(book)

def print_cheapest_books():
    logger.info('Finding cheapest books by price')
    cheapest_Books = sorted(books, key=lambda x: x.price)[:10]
    print('---Cheapest Books---')
    for book in cheapest_Books:
        print(book)

books_gen = (x for x in books)

def print_next_book():
    logger.info('Finding the next available book')
    print(next(books_gen))

CHOICES = {
    'b': print_best_books,
    'c': print_cheapest_books,
    'n': print_next_book,
}

def menu():
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input in ('b', 'c', 'n'):
            CHOICES[user_input]()
        else:
            print('Unkown command. Please try again.')
        user_input = input(USER_CHOICE)

menu()