
from context import wordreference

from lxml import html

import unittest
from unittest.mock import MagicMock

class DataStructureTest(unittest.TestCase):
    in_tr = [['coucou'], ['oiseau'], ['cuckoo'], ['Le coucou pond dans le nid d\'un autre oiseau.', 'The cuckoo lays its eggs in another bird\'s nest.']]
    out = 'coucou\toiseau\tcuckoo\n\tLe coucou pond dans le nid d\'un autre oiseau.\t\n\tThe cuckoo lays its eggs in another bird\'s nest.\t\n'

    def test_translation(self):
        tr = wordreference.datastructure.Translation(*self.in_tr)
        output = tr.__str__()
        print(tr)
        self.assertEqual(self.out, output)


if __name__ == '__main__':
    unittest.main()
