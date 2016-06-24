
import os
import urllib, requests
from lxml import html

class WordReference(object):

    """Class for translating a word from http://www.wordreference.com"""

    def __init__(self, dic, word):
        """Constructor"""
        self._url = 'http://www.wordreference.com/'
        self._articles = None
        self.dic = dic
        self.word = word

    @property
    def dic(self):
        return self._dic

    @dic.setter
    def dic(self, str_dic):
        self._dic = str_dic

    @property
    def word(self):
        return self._word

    @word.setter
    def word(self, str_word):
        self._word = str_word

    @property
    def url(self):
        part_url = os.path.join(self.dic, self.word)
        return urllib.parse.urljoin(self._url, part_url)

    def retrieve_html(self):
        req = requests.get(self.url)
        return html.fromstring(req.content)

    def parse(self):
        html_tree = self.retrieve_html()
