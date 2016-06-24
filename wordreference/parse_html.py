
import os, urllib, requests, argparse
from lxml import html

def parse_argument():
    parser = argparse.ArgumentParser(
            description='process Word Reference html page')
    parser.add_argument('dic', nargs='?', default='fren',
            help='From|To dictionary')
    parser.add_argument('word', nargs='?', default='coucou',
            help='Word to translate')
    return parser.parse_args()

def retrieve_html(dic, word, url='http://www.wordreference.com/'):
    part_url = os.path.join(dic, word)
    complete_url = urllib.parse.urljoin(url, part_url)
    req = requests.get(complete_url)
    html_body = req.content
    tree = html.fromstring(html_body)
    return tree

def retrieve_tables(html_tree):
    tables = html_tree.xpath('//table[@class="WRD"]')
    return [retrieve_cells(table) for table in tables]

def retrieve_cells(html_tree):
    cells = html_tree.xpath('./tr[@class="even" or "odd"]')
    return [parse_cell(x) for x in cells]

def parse_cell(html_tree):
    # try:
        # print(html_tree.get_element_by_id('fren:23249'))
        # print(html_tree.text_content())
    # except Exception as e:
        # pass
    print(html_tree.get('id'))
    frwords = retrieve_FrWrd(html_tree)
    towords = retrieve_ToWrd(html_tree)
    frex = retrieve_FrEx(html_tree)
    toex = retrieve_ToEx(html_tree)
    return [frwords, towords, frex, toex]

def retrieve_FrWrd(html_tree):
    """Retrieve word to translate

    :html_tree: current html cell
    :returns: list of word to translate

    """
    return html_tree.xpath('./td[@class="FrWrd"]/strong/text()')

def retrieve_ToWrd(html_tree):
    """Retrieve translated word

    :html_tree: current html cell
    :returns: list of translated word

    """
    return html_tree.xpath('./td[@class="ToWrd"]/text()')

def retrieve_FrEx(html_tree):
    """Retrieve word to translate use examples

    :html_tree: current html cell
    :returns: list of word to translate use examples

    """
    return html_tree.xpath('./td[@class="FrEx"]/text()')

def retrieve_ToEx(html_tree):
    """Retrieve translated word use examples

    :html_tree: current html cell
    :returns: list of translated word use examples

    """
    return html_tree.xpath('./td[@class="ToEx"]/text()')

if __name__ == '__main__':
    args = parse_argument()
    html_tree = retrieve_html(args.dic, args.word)
    info = retrieve_tables(html_tree)
    # print(info)
    # for inf in info:
        # for i in inf:
            # print(i)
