
from context import wordreference

from lxml import html

import unittest
from unittest.mock import MagicMock

class DataWrapperTest(unittest.TestCase):

    def test_retrievehtml(self):
        WrdRef = wordreference.wordreference.WordReference('fren', 'coucou')
        self.assertEqual(WrdRef.url,
                'http://www.wordreference.com/fren/coucou')
        html_node = WrdRef.retrieve_html()
        WrdRef.parse(html_node)
        str_list = []
        # for node in WrdRef._node_list:
            # print(node.get('class'))
            # print(node.text_content())

if __name__ == '__main__':
    unittest.main()
