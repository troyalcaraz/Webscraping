import re

from locators.book_locators import BookLocators

class BookParser:
    '''Given one of the specific book divs, find out the data about
    the book (title, price, rating, in-stock).'''

    RATINGS = {
        'One':1,
        'Two':2,
        'Three':3,
        'Four':4,
        'Five':5
    }

    def __init__(self, parent):
        self.parent = parent

    def __repr__(self):
        return f'<Book {self.title}, for ${self.price} ({self.rating} stars)>'

    @property
    def title(self):
        locator = BookLocators.TITLE
        book_link = self.parent.select_one(locator)
        book_title = book_link.attrs['title']
        return book_title

    @property
    def price(self):
        locator = BookLocators.PRICE
        item_price = self.parent.select_one(locator).string

        pattern = '([0-9]+\.[0-9]+)'
        matcher = re.search(pattern, item_price)
        return float(matcher.group(0))

    @property
    def link(self):
        locator = BookLocators.LINK
        item_link = self.parent.select_one(locator).attrs['href']
        return item_link

    @property
    def rating(self):
        locator = BookLocators.RATING
        star_rating_tag = self.parent.select_one(locator)
        classes = star_rating_tag.attrs['class']
        star_rating = [e for e in classes if e != 'star-rating']
        rating_number = BookParser.RATINGS.get(star_rating[0], -1)
        return rating_number