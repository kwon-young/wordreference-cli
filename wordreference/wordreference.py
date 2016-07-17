
import os
import six.moves.urllib as urllib
import requests
from lxml import html

class WordReference(object):

    """Class for translating a word from http://www.wordreference.com"""

    def __init__(self, dic, word):
        """Constructor"""
        self._url = 'http://www.wordreference.com/'
        self._dic = dic
        self._word = word
        self._lines_classes = ['even', 'odd', 'wrtopsection', 'langHeader']
        classes = '" or "'.join(self._lines_classes)
        self._xpaths = [
                '//div[@id="articleWRD"]',
                './table[@class="WRD"]',
                './tr[@class="' + ''.join(classes) + '"]',
                './td',
                ]
        self._node_list = []
    @property
    def url(self):
        part_url = os.path.join(self._dic, self._word)
        return urllib.parse.urljoin(self._url, part_url)

    def retrieve_html(self):
        req = requests.get(self.url)
        return html.fromstring(req.content)

    def parse(self, html_node, lvl=0):
        """parse an WordReference html page

        """
        if lvl < len(self._xpaths):
            node_list = html_node.xpath(self._xpaths[lvl])
            for node in node_list:
                self.parse(node, lvl+1)
        else:
            self._node_list.append(html_node)
        return self._node_list[3:]
