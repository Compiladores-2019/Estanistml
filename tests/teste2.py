from estanistml import var, env, Symbol, parse, eval #, lex
from hyperpython import h
from lark import Lark, UnexpectedInput
import estanistml.parser
run = lambda src, env=None: eval(parse(src), env)
x, y, a, b, c, f, g, op, alexandre, mo, jao, cristo, classe,ID= map(Symbol, 'x y a b c f g op alexandre mo jao cristo classe ID'.split())

def pretty(x):
    try:
        return x.pretty()
    except AttributeError:
        return str(x)

class EstanistmlSyntaxError(SyntaxError):
    def __str__(self):
        context, line, column = self.args
        return '%s at line %s, column %s.\n\n%s' % (self.label, line, column, context)

class EstanistmlMissOpening(EstanistmlSyntaxError):
    label = 'Missing Opening'

#class EstanistmlMissClosing(EstanistmlSyntaxError):
#    label = 'Missing Closing'

#class EstanistmlMissComma(EstanistmlSyntaxError):
#    label = 'Missing Comma'

#class EstanistmlTrailingComma(EstanistmlSyntaxError):
#    label = 'Trailing Comma'
#class EstanistmlMissValue(EstanistmlSyntaxError):
#    label = 'Missing Value'

def parse_test(estanistml_text):
    try:
        src = parse(estanistml_text)
    except UnexpectedInput as x:
        exc_class = x.match_examples(estanistml.parse(estanistml_text))
        if not exc_class:
            raise
        raise exc_class(x.get_context(estanistml_text), x.line, x.column)

def test():
    try:
        parse_test('x = h1 "bar";')
    except EstanistmlMissOpening as e:
        print(e)


if __name__ == '__main__':
    test()