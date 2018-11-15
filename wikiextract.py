"""
download wikipedia dump and put it in neo4j
"""

from lxml import etree
from py2neo import Graph, Node, Relationship

def fast_iter(context, func, *args, **kwargs):
    """
    Based on Liza Daly's fast_iter
    http://www.ibm.com/developerworks/xml/library/x-hiperfparse/
    See also http://effbot.org/zone/element-iterparse.htm
    """
    for event, elem in context:
        print(event)
        print(elem)
        func(elem, *args, **kwargs)
        # It's safe to call clear() here because no descendants will be accessed
        elem.clear()
        # Also eliminate now-empty references from the root node to elem
        for ancestor in elem.xpath('ancestor-or-self::*'):
            while ancestor.getprevious() is not None:
                del ancestor.getparent()[0]
    del context

def push_in_neo4j(item):
    print(item)

def main():
    db = Graph(password='meetsys')
    prefix = '{http://www.mediawiki.org/xml/export-0.10/}'
    context = etree.iterparse('/home/user/Data/wikipedia/enwiki-20181101-pages-articles1.xml-p10p30302')
    #fast_iter(context, push_in_neo4j)
    for event, elem in context:
        print(elem.text)

if __name__ == "__main__":
    main()
