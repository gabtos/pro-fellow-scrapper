from requests_html import HTMLSession
from bs4 import BeautifulSoup as bs

URL = 'https://www.profellow.com/fellowship/?page=1'


def main():
    print('hello world')
    session = HTMLSession()

    r = session.get(URL)
    print(r.html)


if __name__ == "__main__":
    main()