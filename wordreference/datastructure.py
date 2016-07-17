
from six.moves import zip_longest

class Translation(object):

    """Contain a translation of a word"""

    def __init__(self, frwrds, syns, towrds, exs):
        """Constructor

        :frwrd: TODO
        :syn: TODO
        :towrd: TODO
        :ex: TODO

        """
        self._frwrds = frwrds
        self._syns = syns
        self._towrds = towrds
        self._exs = exs

    def __str__(self):
        """pretty printing

        """
        out_str = ''
        r = max(len(self._syns), len(self._towrds))
        r -= min(len(self._syns), len(self._towrds))
        syn_ex = list(self._syns)
        for i in range(r):
            syn_ex.append('')
        syn_ex += self._exs
        l_wrd, l_syn = self.longest_syn()
        for frwrd, syn_ex, towrd in zip_longest(self._frwrds,
                syn_ex, self._towrds, fillvalue=''):
            spaces = ' ' * (l_wrd - len(frwrd))
            out_str += frwrd+spaces+syn_ex
            if towrd != '':
                spaces = ' ' * (l_syn - len(syn_ex))
                out_str += spaces+towrd
            out_str+='\n'
        return out_str

    def longest_syn(self):
        longest_syn = 0
        syn_ex = list(self._syns) + self._exs
        for syn in syn_ex:
            if len(syn) > longest_syn:
                longest_syn = len(syn)
        longest_word = 0
        for wrd in self._frwrds:
            if len(wrd) > longest_word:
                longest_word = len(wrd)
        return longest_word+3, longest_syn+3

class ListTranslation(object):

    """List of translation"""

    def __init__(self, list_trans):
        """Constructor

        :list_trans: TODO

        """
        self._list_trans = []
        for trans in list_trans:
            self._list_trans.append(Translation(*trans))

    def __str__(self):
        """Pretty printing
        :returns: TODO

        """
        output = ''
        for trans in self._list_trans:
            output += trans.__str__()
        return output
