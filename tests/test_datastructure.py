
from context import wordreference

from lxml import html

import unittest
from unittest.mock import MagicMock

class DataStructureTest(unittest.TestCase):
    in_tr = [['coucou'], ['oiseau'], ['cuckoo'], ['Le coucou pond dans le nid d\'un autre oiseau.', 'The cuckoo lays its eggs in another bird\'s nest.']]
    in_tr2 = [['coucou'], ['horloge'], ['cuckoo clock'], ['Écoute, le coucou sonne 7 heures.', 'Listen, the cuckoo clock is striking 7 o\'clock.',]]
    out = """coucou   oiseau                                             cuckoo
         Le coucou pond dans le nid d'un autre oiseau.
         The cuckoo lays its eggs in another bird's nest.
"""
    outs = """coucou   oiseau                                             cuckoo
         Le coucou pond dans le nid d'un autre oiseau.
         The cuckoo lays its eggs in another bird's nest.
coucou   horloge                                           cuckoo clock
         Écoute, le coucou sonne 7 heures.
         Listen, the cuckoo clock is striking 7 o'clock.
"""

    def test_translation(self):
        print()
        tr = wordreference.datastructure.Translation(*self.in_tr)
        output = tr.__str__()
        print(tr)
        self.assertEqual(self.out, output)

    def test_listTranslation(self):
        print()
        trs = wordreference.datastructure.ListTranslation(
                [self.in_tr, self.in_tr2])
        output = trs.__str__()
        print(trs)
        self.assertEqual(self.outs, output)


if __name__ == '__main__':
    unittest.main()
