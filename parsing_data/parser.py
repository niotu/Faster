from random import randint

import lxml.html
import requests

from const.CONSTANTS import BASE_URL


class Parser:
    def __init__(self):
        self.url0 = BASE_URL
        self.text = None
        self.session = requests.session()

    def get_txt_from_url(self, url: str):
        r = self.session.get(url, timeout=(3.05, 7.05))

        return lxml.html.document_fromstring(r.text)

    def get_titles_urls(self, url):
        soup = self.get_txt_from_url(url)
        titles_url = soup.xpath('//li/a[@class="poemlink"]/@href')
        return titles_url

    def get_text_by_title_url(self, title_url):
        url = self.url0 + title_url
        soup = self.get_txt_from_url(url)
        text = soup.xpath('//div[@class="text"]/text()')
        return text

    def parse(self):
        urls = self.get_titles_urls(self.url0)
        selected_url = urls[randint(0, len(urls) - 1)]
        text = self.get_text_by_title_url(selected_url)
        return text

    def format_text(self, text):
        res = []
        c = 0
        for word in text:
            pass
            if word == '\n':
                c += 1
            elif c == 2:
                break
            else:
                res.append(word[1:].rstrip() + '\n')
        return ''.join(res)

    def write_text(self, text):
        self.text = text
        # with open('parsed_text.txt', 'w', encoding=ENCODING) as f:
        #     f.write(text)

    def process(self):
        rude_text = self.parse()
        text = self.format_text(rude_text)
        self.write_text(text)

# parser = Parser()
# parser.process()
# sleep(2.0)
# with open('parsed_text.txt', 'r', encoding=ENCODING) as f:
#     mas = f.read()
# mas = ''.join(mas).split('\n')
# mas.remove('')
# print(mas)
