
from collections import deque
import difflib

class Interface(object):

    """Interface between WordReference and ListTranslation"""

    def __init__(self):
        """Constructor """
        self._header      = [['FrWrd', None, 'ToWrd']]
        self._header_rest = [[None, None, 'ToWrd'], [None, 'To2', 'ToWrd']]
        self._example     = [[None, 'ToEx'], [None, 'FrEx']]
        # self._notePublic  = [['notePubl']]
        self._list_seq = [self._header,
                          self._header_rest,
                          self._example,
                          # self._notePublic,
                          ]
        self._list_extract = [
                self.extract_header,
                self.extract_header_rest,
                self.extract_example,
                ]
        self._list_struct = []

    def extract_header(self, seq):
        frwrd = seq[0].xpath('./strong/text()')
        syn = [seq[1].text_content()]
        towrd = seq[2].xpath('./text()')
        self._list_struct.append([frwrd, syn, towrd, []])

    def extract_header_rest(self, seq):
        self._list_struct[-1][2].append(seq[2].xpath('./text()')[0])
        if seq[1].get('class') == 'To2':
            syn = seq[1].text_content()
            self._list_struct[-1][1].append(syn)

    def extract_example(self, seq):
        self._list_struct[-1][3].append(seq[1].text_content())
        pass

    def treatement(self, string):
        return string.replace(u'\xa0', u' ').strip()

    def post_treatment(self, lst_i=[]):
        self._list_struct = [[[self.treatement(z) for z in y]
            for y in x]
            for x in self._list_struct]

    def longest_seq(self):
        max_len = 0
        for lst in self._list_seq:
            for seq in lst:
                if len(seq) > max_len:
                    max_len = len(seq)
        return max_len

    def smallest_seq(self):
        min_len = 999999
        for lst in self._list_seq:
            for seq in lst:
                if len(seq) < min_len:
                    min_len = len(seq)
        return min_len

    def iter_seq(self):
        for i, seqs in enumerate(self._list_seq):
            for seq in seqs:
                yield i, seq

    def match_seq(self, seq):
        for i, seq2 in self.iter_seq():
            if seq[:len(seq2)] == seq2:
                # print(seq[:len(seq2)], seq2)
                return i
        return None

    def convert(self, node_list):
        node_seq = deque(maxlen=self.longest_seq())
        for i in range(self.longest_seq() - self.smallest_seq()):
            node_list.append(node_list[-2])
        for node in node_list:
            node_seq.append(node)
            i = self.match_seq([n.get('class') for n in node_seq])
            if i is not None:
                self._list_extract[i](node_seq)
        self.post_treatment()
        # print(self._list_struct)
        return self._list_struct
