from lark import Lark, InlineTransformer
from pathlib import Path

from .runtime import Symbol

class LispTransformer(InlineTransformer):
    def start(self, *args): 
        try:
            return ["macro", *args]
        except ValueError:
            return ["import", *args]
        

    def string(self, st):
        res = str(st)[1:-1]
        res = res.replace("\\n","\n").replace("\\t","\t").replace("\\","")
        return res
    
    def numb(self, number):
        try:
            return int(number)
        except ValueError:
            return float(number)
    
    def args(self, *args):
        return ("args", *args)
    

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

parser = _make_grammar()