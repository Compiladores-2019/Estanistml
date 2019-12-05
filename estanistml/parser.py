from lark import Lark, InlineTransformer
from pathlib import Path
from .runtime import Symbol
# from html.parser import HTMLParser
# from bs4 import BeautifulSoup

# class MyHTMLParser(HTMLParser):
#     def handle_starttag(self, tag, attrs):
#         print(tag)
#         return tag
#     def handle_endtag(self, endtag):
#        print(endtag)
#        return endtag
#     def handle_data(self, data):
#         print(data)
#         return data

class LispTransformer(InlineTransformer):
    int = int
    float = float
    name = Symbol

    def start(self, *args): 
        return ['module', *args]
        
    def string(self, st):
        res = str(st)[1:-1]
        res = res.replace("\\n","\n").replace("\\t","\t").replace("\\","")
        return res
    
    def args(self, *args):
        return list(args)
    
    def define(self, name, x):
        return ['define', name, x]

    def macro(self, name, args, expr):
        return ['macro', name, args, expr]
    
    def param(self, name, expr):
        return (name, expr)
    
    def atrib(self, *param):
        return list(param)

#name atrib children? -> html_full

    def html_full(self, tag, atrib, children):
        return ['html', str(str(tag)),{str(atrib)},children]

    def html_simple(self, tag, children=None):
        return ['html', str(str(tag)), {}, children or []]

    def children(self, *args):
        return list(args)

    # def atom(self, args):
    #     print("aq")
    #     try:
    #         return self.numb(args)
    #     except ValueError:
    #         try:
    #             res = str(args)[1:-1]
    #             res = res.replace("\\n","\n").replace("\\t","\t").replace("\\","")
    #             return res
    #         except ValueError:
    #             return list(args)


    # def obj(self, *args):
    #     return dict(*args)
   

    

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


def lex(src: str):
    return list(parser.lex(src))

parser = _make_grammar()