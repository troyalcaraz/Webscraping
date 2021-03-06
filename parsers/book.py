import re
import logging

from locators.book_locators import BookLocators

logger = logging.getLogger('scaping.book_parser')

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
        logger.debug(f'New book parser created from `{parent}`.')
        self.parent = parent

    def __repr__(self):
        return f'<Book {self.title}, for ${self.price} ({self.rating} stars)>'

    @property
    def title(self):
        logger.debug('Finding book name...')
        locator = BookLocators.TITLE
        book_link = self.parent.select_one(locator)
        book_title = book_link.attrs['title']
        logger.debug(f'Found book name, `{book_title}`.')
        return book_title

    @property
    def price(self):
        logger.debug('Finding book price...')
        locator = BookLocators.PRICE
        item_price = self.parent.select_one(locator).string

        pattern = '([0-9]+\.[0-9]+)'
        matcher = re.search(pattern, item_price)
        logger.debug(f'Found book price, `{matcher.group(0)}`.')
        return float(matcher.group(0))

    @property
    def link(self):
        logger.debug('Finding book link...')
        locator = BookLocators.LINK
        item_link = self.parent.select_one(locator).attrs['href']
        logger.debug(f'Found book link, `{item_link}`.')
        return item_link

    @property
    def rating(self):
        logger.debug('Finding book rating...')
        locator = BookLocators.RATING
        star_rating_tag = self.parent.select_one(locator)
        classes = star_rating_tag.attrs['class']
        star_rating = [e for e in classes if e != 'star-rating']
        rating_number = BookParser.RATINGS.get(star_rating[0], -1)
        logger.debug(f'Found book rating, `{rating_number}`.')
        return rating_number