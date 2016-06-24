
from context import wordreference

from lxml import html

import unittest
from unittest.mock import MagicMock

class DataWrapperTest(unittest.TestCase):

    def test_wordreference(self):
        WrdRef = wordreference.wordreference.WordReference('fren', 'coucou')
        self.assertEqual(WrdRef.url,
                'http://www.wordreference.com/fren/coucou')
        with open('tests/coucou.html') as f:
            WrdRef.retrieve_html = MagicMock(name='retrieve_html',
                    return_value=html.fromstring(f.read()))
        WrdRef.parse()
        WrdRef.retrieve_html.assert_called_once_with()


if __name__ == '__main__':
    unittest.main()
