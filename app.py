import requests

from pages.books_page import BookPage

page_content = requests.get('https://books.toscrape.com').content
page = BookPage(page_content)

books = page.books

for page_num in range(1, page.page_count):
    url = f'https://books.toscrape.com/catalogue/page-{page_num+1}.html'
    page_content = requests.get(url).content
    page = BookPage(page_content)
    books.extend(page.books)