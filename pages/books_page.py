from bs4 import BeautifulSoup
import re
import logging

from locators.book_page_locator import BookPageLocator
from parsers.book import BookParser

logger = logging.getLogger('scraping.all_books_page')

class BookPage:
    def __init__(self, page):
        self.soup = BeautifulSoup(page, 'html.parser')
        logger.debug('Parsing page content with BeautifulSoup HTML parser')

    @property
    def books(self):
        logger.debug(f'Finding all books in the page using `{BookPageLocator.BOOK}`.')
        locator = BookPageLocator.BOOK
        book_tags = self.soup.select(locator)
        return [BookParser(e) for e in book_tags]

    @property
    def page_count(self):
        logger.debug('Finding all number of catalogue pages available...')
        content = self.soup.select_one(BookPageLocator.PAGER).string
        pattern = 'Page [0-9]+ of ([0-9]+)'
        logger.info(f'Found number of catalogue pages available: `{content}`.')
        matcher = re.search(pattern, content)
        pages = int(matcher.group(1))
        logger.debug(f'Extracted number of pages as integer `{pages}`.')
        return pages
