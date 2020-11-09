from app import books

USER_CHOICE = '''Enter one of the following
- 'b' to look at 5-star books
- 'c' to look at the cheapest books
- 'n' to just get the nect available book on the catalouge
- 'q' to quit

Enter your choice: '''

def print_best_books():
    best_books = sorted(books, key=lambda x: x.rating * -1)[:10]
    print('---Best Books---')
    for book in best_books:
        print(book)

def print_cheapest_books():
    cheapest_Books = sorted(books, key=lambda x: x.price)[:10]
    print('---Cheapest Books---')
    for book in cheapest_Books:
        print(book)

books_gen = (x for x in books)

def print_next_book():
    print(next(books_gen))

def menu():
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input == 'b':
            print_best_books()
        elif user_input == 'c':
            print_cheapest_books()
        elif user_input == 'n':
            print_next_book()
        else:
            print('Unkown command. Please try again.')
        user_input = input(USER_CHOICE)

menu()