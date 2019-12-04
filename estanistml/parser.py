from lark import Lark, InlineTransformer
from pathlib import Path
from .runtime import Symbol
from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        return tag
    def handle_endtag(self, endtag):
       print(endtag)
       return endtag
    def handle_data(self, data):
        print(data)
        return data

class LispTransformer(InlineTransformer):
    parser = MyHTMLParser()
    parser.feed('<html><head><title>Test</title></head></html>')
    def start(self, *args): 
        return ["Macro", *args]

    def string(self, st):
        return st[1:-1]  

   

    

def parse(src: str):
    """
    Compila string de entrada e retorna a S-expression equivalente.
    """
    return parser.parse(src)


def _make_grammar():
    """
    Retorna uma gramática do Lark inicializada.
    """

    path = Path(__file__).parent / 'grammar.lark'
    with open(path) as fd:
        grammar = Lark(fd, parser='lalr', transformer=LispTransformer())
    return grammar

parser = _make_grammar()