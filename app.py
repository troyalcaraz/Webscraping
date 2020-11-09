import requests

from pages.books_page import BookPage

page_content = requests.get('http://books.toscrape.com').content
page = BookPage(page_content)

books = page.books