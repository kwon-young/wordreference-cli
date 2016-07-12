
from context import wordreference

from lxml import html

import unittest
from unittest.mock import MagicMock

class InterfaceTest(unittest.TestCase):
    result = [
            [['coucou'], ['(oiseau)'], ['cuckoo'], ['Le coucou pond dans le nid d\'un autre oiseau.', 'The cuckoo lays its eggs in another bird\'s nest.']],
            [['coucou'], ['(horloge)'], ['cuckoo clock'], ['Écoute, le coucou sonne 7 heures.', 'Listen, the cuckoo clock is striking 7 o\'clock.']],
            [['coucou'], ['(fleur : primevère sauvage)'], ['cowslip', 'wild daffodil', 'wild narcissus'], ['Les coucous poussent au bord des chemins.', 'Cowslips are growing by the side of the paths.']],
            [['coucou'], ['familier (avion vétuste) (informal, figurative: aircraft)'], ['old crate'], ['Nous avons fait un tour en brousse dans un vieux coucou.', 'We did a tour of the bush in an old crate.']],
            [['coucou'], ['familier (me voilà)', '(informal)'], ['Hey there!', 'cooee', 'hello'], ['Coucou, c\'est moi !', 'Hey there, it\'s me!', 'Cooee, it\'s me!', 'Hello, it\'s me!']],
            ]

    def test_min_max_seq(self):
        interface = wordreference.interface.Interface()
        self.assertEqual(interface.longest_seq(), 3)
        self.assertEqual(interface.smallest_seq(), 2)

    def test_convert(self):
        WrdRef = wordreference.wordreference.WordReference('fren', 'coucou')
        html_node = WrdRef.retrieve_html()
        node_list = WrdRef.parse(html_node)
        interface = wordreference.interface.Interface()
        lst_result = interface.convert(node_list)
        self.assertEqual(lst_result, self.result)
        trs = wordreference.datastructure.ListTranslation(lst_result)
        # print(trs)


if __name__ == '__main__':
    unittest.main()
