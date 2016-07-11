
from itertools import zip_longest

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
        syn_ex = self._syns + self._exs
        for frwrd, syn_ex, towrd in zip_longest(self._frwrds,
                syn_ex, self._towrds, fillvalue=''):
            out_str += '\t'.join([frwrd, syn_ex, towrd])+'\n'
        return out_str

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
