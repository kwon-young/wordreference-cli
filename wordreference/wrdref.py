#!/usr/bin/env python
# __          __      _ _____       __    _____ _      _____ 
# \ \        / /     | |  __ \     / _|  / ____| |    |_   _|
#  \ \  /\  / / __ __| | |__) |___| |_  | |    | |      | |  
#   \ \/  \/ / '__/ _` |  _  // _ \  _| | |    | |      | |  
#    \  /\  /| | | (_| | | \ \  __/ |   | |____| |____ _| |_ 
#     \/  \/ |_|  \__,_|_|  \_\___|_|    \_____|______|_____|
# Little cli tool for translating a word with http://www.wordreference.com
# Version: 0.1.0
# Author:  Kwon-Young Choi
# URL:     https://github.com/kwon-young/wordreference-cli

import argparse
from . import wordreference
from . import interface
from . import datastructure
# import wordreference
# import interface
# import datastructure

def parse_argument():
    parser = argparse.ArgumentParser(
            description='process Word Reference html page')
    parser.add_argument('dic', nargs='?', default='fren',
            help='From|To dictionary')
    parser.add_argument('word', nargs='?', default='coucou',
            help='Word to translate')
    return parser.parse_args()

def translate(dic, word):
    WrdRef = wordreference.WordReference(dic, word)
    html_node = WrdRef.retrieve_html()
    node_list = WrdRef.parse(html_node)
    interf = interface.Interface()
    lst_result = interf.convert(node_list)
    trs = datastructure.ListTranslation(lst_result)
    out = trs.__str__()
    return out

def main():
    args = parse_argument()
    out = translate(args.dic, args.word)
    print(out)

if __name__ == '__main__':
    main()
