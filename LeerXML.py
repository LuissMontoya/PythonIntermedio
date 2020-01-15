# -*- coding: utf-8 -*-

from xml.dom.minidom import parse,Node

if __name__ == "__main__":
    xmltree=parse('private.xml')
    for nodo in xmltree.getElementsByTagName('ustring'):
        for nodo_hijo in nodo.childNodes:
            if nodo_hijo.nodeType==Node.TEXT_NODE:
                print(nodo_hijo.data)