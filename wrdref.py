
import argparse
import wordreference

def parse_argument():
    parser = argparse.ArgumentParser(
            description='process Word Reference html page')
    parser.add_argument('dic', nargs='?', default='fren',
            help='From|To dictionary')
    parser.add_argument('word', nargs='?', default='coucou',
            help='Word to translate')
    return parser.parse_args()

if __name__ == '__main__':
    args = parse_argument()
    WrdRef = wordreference.wordreference.WordReference(args.dic, args.word)
    html_node = WrdRef.retrieve_html()
    node_list = WrdRef.parse(html_node)
    interface = wordreference.interface.Interface()
    lst_result = interface.convert(node_list)
    trs = wordreference.datastructure.ListTranslation(lst_result)
    print(trs)
